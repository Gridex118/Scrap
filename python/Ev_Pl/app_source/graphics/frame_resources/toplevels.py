# Graphics for Event Planner - Pop_ups

# _____________________________ Imports

from tkinter import Toplevel
from app_source.graphics.frame_resources.specials import DragRegion, TitleBar
from app_source.graphics.frame_resources.toplevel_frames import *
from time import sleep

# _____________________________ Classes

class Popup(Toplevel):

    def __init__(self,parent,width=400,height=200):
        super().__init__()
        self.parent = parent
        self.system = self.parent.system
        self.overrideredirect(1)
        self.wm_attributes('-alpha', 0.95)
        self.wm_attributes('-topmost',True)
        self.width = width
        self.height = height
        x_corr = (self.winfo_screenwidth()-self.width)/2
        y_corr = (self.winfo_screenheight()-self.height)/2
        self.geometry('%dx%d+%d+%d' % (self.width,self.height,x_corr,y_corr))
        self.config(bg='black')


class ErrorPopUp(Popup):

    def __init__(self,parent,text):
        super().__init__(parent)
        self.config(bg='firebrick1')
        self.frame = PopUpErrorFrame(self, text=text)
        self.frame.grid(row=0,column=0,pady=(2,0))

    def buttonConfig(self,command):
        self.frame.button.config(command=command)


class Floater(Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.x_corr = self.winfo_screenwidth() - 20
        self.y_corr = 10
        self.width = 20
        self.height = 70
        self.geometry(f'{self.width}x{self.height}+{self.x_corr}+{self.y_corr}')
        self.config(bg='#10E0DA')
        self.wm_attributes('-alpha', 0.5)
        self.wm_attributes('-topmost', True)
        self.overrideredirect(True)
        self.drag_region = DragRegion(self, self, self.width, self.height, 'y')
        self.drag_region.grid()
        for widget in (self, self.drag_region):
            widget.bind('<Control-1>', lambda ev: parent.app.maximize(self))


class SqlPassPop(Toplevel):

    def __init__(self, parent, loader):
        super().__init__(parent)
        self.app = parent
        self.system = parent.system
        self.loader = loader
        self.width = 600
        self.height = 200
        x_corr = (self.winfo_screenwidth() - self.width)/2
        y_corr = (self.winfo_screenheight() - self.height)/2
        self.geometry(f'{self.width}x{self.height}+{int(x_corr)}+{int(y_corr)}')
        self.overrideredirect(True)
        self.wm_attributes('-alpha', 0.980)
        self.wm_attributes('-topmost', True)
        self.pass_frame = MySqlPassFrame(self)
        self.pass_frame.grid()
        self.loader.state('withdrawn')

    def close(self):
        self.loader.state('normal')
        self.destroy()


class SpecialToplevel(Toplevel):

    def __init__(self, parent, width, height):
        super().__init__(parent)
        self.parent = parent
        self.system = self.parent.system
        self.memory = self.system.memory
        self.wm_attributes('-topmost', True)
        self.width = width
        self.height = height
        self.x_corr = (self.winfo_screenwidth()-self.width)/2
        self.y_corr = (self.winfo_screenheight()-self.height)/2
        self.geometry(f"{self.width}x{self.height}+{int(self.x_corr)}+{int(self.y_corr)}")
        self.overrideredirect(True)


class CardEditor(SpecialToplevel):

    def __init__(self, parent, card_type):
        super().__init__(parent, 800, 490)
        self.app = self.parent.app
        TitleBar(self, restrict_minimization=True).grid(row=0, column=0, columnspan=2)
        self.edited_card_type_value = card_type[:(-1)]
        self.position_sub_frame(CardDescFrame, 'alpha', self.edited_card_type_value)
        if self.edited_card_type_value == 'event':
            self.position_sub_frame(EventParaFrame, 'beta')
        elif self.edited_card_type_value == 'task':
            self.position_sub_frame(TaskParaFrame, 'beta')
        elif self.edited_card_type_value == 'reminder':
            self.position_sub_frame(ReminderParaFrame, 'beta')
        elif self.edited_card_type_value == 'note':
            self.position_sub_frame(NoteParaFrame, 'beta')
        inner.SaveCardValuesButton(self).place(x=235, y=450)
        inner.DiscardCardValuesButton(self).place(x=440, y=450)

    def position_sub_frame(self, sub_frame, position_code='alpha', *args):
        initiated_sub_frame = sub_frame(self, *args)
        if position_code == 'alpha':
            initiated_sub_frame.grid(row=1, column=0, columnspan=2, padx=(5,0), pady=(5,0), sticky='w')
        elif position_code == 'beta':
            initiated_sub_frame.grid(row=2, column=0, columnspan=2, padx=(5,0), pady=(5,0), sticky='w')
        if isinstance(initiated_sub_frame, CardDescFrame):
            self.desc_frame = initiated_sub_frame
        elif isinstance(initiated_sub_frame, CardParaFrame):
            self.para_frame = initiated_sub_frame

    def feed_values_to_system(self):
        self.system.create_card(
            self.edited_card_type_value, self.desc_frame.get_values(), self.para_frame.get_values()
        )
        self.shutdown()

    def shutdown(self):
        self.destroy()


class LoadScreen(SpecialToplevel):

    def __init__(self,parent):
        super().__init__(parent, 550, 250)
        LoadFrame(self).grid()

    def wait(self):
        if (self.system.connected is True) and (self.parent.running is True):
            self.parent.draw_frames()
            self.parent.state('normal')
            self.destroy()
        elif (self.system.connected is False) and (self.parent.running is True):
            sleep(0.5)
            self.wait()

# ___________________________________________________
