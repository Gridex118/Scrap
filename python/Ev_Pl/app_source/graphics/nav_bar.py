# Navigation Bar

# ____________________ Imports

from app_source.graphics.frame_resources.bases import MyFrame, MyButton
import app_source.graphics.frame_resources.inner_frames as inner

# ____________________ Classes

class NavBar(MyFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(bg='#FDFDFD')
        self.config(width=self.parent['width'],height=((4*self.parent['height']/5) - 20))
        self.memory.addProcess('NavBut_disabled',[])
        self.memory.addProcess('NavBut_enabled',None)

    def setButtons(self):
        inner.Padframe(self,width=(self['width'])).grid(row=0,column=0,sticky='w')
        CalendarButton(self).grid(row=1, column=0, sticky='w')
        MyScheduleButton(self).grid(row=2, column=0, sticky='w')
        RemindersButton(self).grid(row=3, column=0, sticky='w')
        NotesButton(self).grid(row=4, column=0, sticky='w')
        MyProfileButton(self).grid(row=5, column=0, sticky='w')
        inner.Padframe(self,width=(self['width'])).grid(row=6,column=0,sticky='w')
        self.config(bg='#109FFF')
        self.reconfigure_navs()

    @property
    def active_nav(self):
        return self.memory.getProcessData('NavBut_enabled')

    def reconfigure_navs(self):
        active_button = self.active_nav
        active_button.config(width=28,bg='#EFEFEF',fg='#00AFE0')
        active_button.bind('<Enter>', lambda ev: None)
        active_button.bind('<Leave>', lambda ev: None)
        active_button.bind('<1>', lambda ev: None)
        self.app.tabs.setTabs(opt_set=active_button.name)
        for inactive_button in self.memory.getProcessData('NavBut_disabled'):
            inactive_button.config(width=30,bg='#FDFDFD')
            inactive_button.bind('<1>', inactive_button.set_as_active)
            inactive_button.bind('<Enter>', inactive_button.on_entering)
            inactive_button.bind('<Leave>', inactive_button.on_leaving)

    def clear_nav_bar(self):
        self.config(bg='#FDFDFD')
        for nav in self.winfo_children():
            nav.destroy()
        self.memory.clearProcess('NavBut_enabled')
        self.memory.clearProcess('NavBut_disabled')


class NavButton(MyButton):

    def __init__(self,parent):
        super().__init__(parent)
        self.name = 'Nav'
        self.config(bg='#FDFDFD')
        self.config(width=30,height=2)
        self.memory.addProcess('NavBut_disabled',self)
        self.bind('<1>', self.set_as_active)

    def set_as_active(self, event):
        self.parent.app.tabs.clearTabs()
        self.memory.shiftData(self.parent.active_nav, 'NavBut_enabled', 'NavBut_disabled')
        self.memory.shiftData(self,'NavBut_disabled','NavBut_enabled')
        self.parent.reconfigure_navs()

    def on_leaving(self,event):
        self.config(bg='#FDFDFD',fg='#00AFE0')


class CalendarButton(NavButton):

    def __init__(self,parent):
        super().__init__(parent)
        self.name = 'calendar'
        self.config(text='Calendar')
        self.memory.shiftData(self,'NavBut_disabled','NavBut_enabled')


class RemindersButton(NavButton):

    def __init__(self,parent):
        super().__init__(parent)
        self.name = 'reminders'
        self.config(text='Reminders')


class NotesButton(NavButton):

    def __init__(self,parent):
        super().__init__(parent)
        self.name = 'notes'
        self.config(text='Notes')


class MyProfileButton(NavButton):

    def __init__(self,parent):
        super().__init__(parent)
        self.name = 'profile'
        self.config(text='My Profile')


class MyScheduleButton(NavButton):

    def __init__(self,parent):
        super().__init__(parent)
        self.name = 'schedule'
        self.config(text='Today\'s Schedule')

# ________________________
