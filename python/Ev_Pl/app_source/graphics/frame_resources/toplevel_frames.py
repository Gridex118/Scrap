# Toplevel Frames - Graphics for Event Planner

# _______________________ Imports

from tkinter import PhotoImage, Label
from app_source.graphics.frame_resources.bases import MyLesserFrame, MyFrame, TitledFrame
import app_source.graphics.frame_resources.inner_frames as inner

# ________________________ Classes

class PopUpErrorFrame(MyLesserFrame):

    def __init__(self,parent,text):
        super().__init__(parent)
        self.config(width=(99 * self.parent.width / 100), height=(99 * self.parent.height / 100))
        self.config(bg='#FCFCFC')
        inner.MyLabel(self, text, size=15,color='#10DFFA').grid(
            row=0, column=0, columnspan=2, padx=(40,0), pady=(50,0)
        )
        self.button = inner.OkButton(self)
        self.button.grid(row=1, column=0, padx=(140,0), pady=(50,0))


class LoadFrame(MyLesserFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(bg='#FAFAFA')
        self.config(width=550,height=250)
        self.bg_img = PhotoImage(file='app_source/graphics/assets/loader.png')
        Label(self, image=self.bg_img).grid()


class MySqlPassFrame(MyFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(width=parent.width, height=parent.height)
        self.config(bg='#FFFFFF')
        self.passwd = inner.TextEntry(self, header='MySQL Password')
        self.passwd.grid_propagate(0)
        self.passwd.place(x=50, y=70)
        self.enter = inner.MySqlPassEnterButton(self)
        self.enter.place(x=130,y=130)
        self.cancel = inner.MySqlPassCancelButton(self)
        self.cancel.place(x=310, y=130)

    def enterPass(self):
        self.app.feed_passwd_to_sys(self.passwd.get())
        self.parent.close()


class CardDescFrame(TitledFrame):

    def __init__(self, parent, card_type):
        titled_card_type = card_type.title()
        super().__init__(
            parent, width=(parent.width - 10),
            height=((450*3/5)-10),
            text=f"{titled_card_type} Description"
        )
        self.record_name = inner.TextEntry(self, f"{titled_card_type} Name", width=300)
        self.record_desc = inner.TextEntry(
            self, f"{titled_card_type} Description",
            width=(self['width'] - 40), height=(self['height'] - 100)
        )
        self.record_name.grid(row=1, column=0, padx=(10, 0), pady=(10, 0), sticky='w')
        self.record_desc.grid(
            row=2, column=0, columnspan=2, rowspan=2, padx=(10, 0), pady=(10, 0), sticky='w'
        )

    def get_values(self):
        return {'name':self.record_name.get(), 'desc': self.record_desc.get()}


class CardParaFrame(TitledFrame):

    def __init__(self, parent, card_type):
        super().__init__(
            parent,
            width=(parent.width - 10),
            height=((450*2/5) - 20),
            text=f"{card_type.title()} Parameters"
        )
        inner.MyLabel(self, text='Date: ').grid(row=1, column=0, padx=(10, 0), pady=(15,0), sticky='w')
        self.date = inner.DateEntry(self)
        self.date.grid(row=1, column=1, columnspan=2, pady=(10,0), sticky='w')

    def get_values(self):
        ...


class EventParaFrame(CardParaFrame):

    def __init__(self, parent):
        super().__init__(parent, 'event')
        inner.MyLabel(self, text='Visible To: ').grid(row=2, column=0, padx=(10,0), pady=(10,0), sticky='w')
        self.visibility = inner.TextEntry(self, 'self/everyone :: Default: self', 'self', 350)
        self.visibility.grid(row=2, column=1, padx=(10,0), pady=(10,0),sticky='w')
        inner.MyLabel(self, text='Create Task: ').grid(row=3, column=0, padx=(10,0), pady=(10,0), sticky='w')
        self.task_bool = inner.TextEntry(self, 'yes/no :: Default: no', 'no', 300)
        self.task_bool.grid(row=3, column=1, padx=(10,0), pady=(10,0), sticky='w')

    def get_values(self):
        return {'date': self.date.get(), 'visibility': self.visibility.get(), 'task': self.task_bool.get()}


class TaskParaFrame(CardParaFrame):

    def __init__(self, parent):
        super().__init__(parent, 'task')
        inner.MyLabel(self, text='Start Time: ').grid(row=2, column=0, padx=(10,0), pady=(10,0), sticky='w')
        self.start_time = inner.TimeEntry(self)
        self.start_time.grid(row=2, column=1,pady=(10,0), sticky='w')
        inner.MyLabel(self, text='End Time: ').grid(row=2, column=2, padx=(10,0), pady=(10,0), sticky='w')
        self.end_time = inner.TimeEntry(self)
        self.end_time.grid(row=2, column=3, pady=(10,0), sticky='w')
        inner.MyLabel(self, 'Priority: ').grid(row=3, column=0, padx=(10,0), pady=(10,0), sticky='w')
        self.priority = inner.TextEntry(self, 'high/mid/low :: Default: mid', 'mid', 250)
        self.priority.grid(row=3, column=1, padx=(10,0), pady=(10,0), sticky='w')
        inner.MyLabel(self, 'Repeat: ').grid(row=3, column=2, padx=(10,0), pady=(10,0), sticky='w')
        self.repeat = inner.TextEntry(self, 'yes/no :: Default: no', 'no', 200)
        self.repeat.grid(row=3, column=3, pady=(10,0), sticky='w')

    def get_values(self):
        return {
            'date': self.date.get(), 'start': self.start_time.get(), 'end': self.end_time.get(),
            'priority': self.priority.get(), 'repeat': self.repeat.get()
        }


class ReminderParaFrame(CardParaFrame):

    def __init__(self, parent):
        super().__init__(parent, 'reminder')
        inner.MyLabel(self, text='Time: ').grid(row=2, column=0, padx=(10,0), pady=(10,0), sticky='w')
        self.time = inner.TimeEntry(self)
        self.time.grid(row=2, column=1, pady=(10, 0), sticky='w')
        inner.MyLabel(self, text='Repeat: ').grid(row=3, column=0, padx=(10,0), pady=(10,0), sticky='w')
        self.repeat = inner.TextEntry(self, 'once/everyday :: Default: once', 'once', 300)
        self.repeat.grid(row=3, column=1, padx=(10,0), pady=(10,0), sticky='w')

    def get_values(self):
        return {
            'date': self.date.get(), 'time': self.time.get(), 'repeat': self.repeat.get()
        }


class NoteParaFrame(CardParaFrame):

    def __init__(self, parent):
        super().__init__(parent, 'note')
        inner.MyLabel(self, text='Recipient:').grid(row=2, column=0, padx=(10,0),pady=(10,0), sticky='w')
        self.recipient = inner.TextEntry(
            self, 'self/user_name/everyone :: Default: self', 'self',350, entry_width=35
        )
        self.recipient.grid(row=2, column=1, padx=(10,0), pady=(10,0), sticky='w')

    def get_values(self):
        return {'date': self.date.get(), 'recipient': self.recipient.get()}

# ________________________
