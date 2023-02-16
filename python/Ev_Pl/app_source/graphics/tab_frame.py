# Tab Frame - Graphics for Event Planner

# __________________________ Imports

from app_source.graphics.frame_resources.bases import MyFrame, MyButton

# __________________________ Classes

class Tab(MyButton):

    def __init__(self,parent):
        super().__init__(parent)
        self.memory.addProcess('Tabs_in_back',self)
        self.config(bg='#FDFDFD',activebackground='#EFEFEF')
        self.config(font=('Ariel',12,'italic'))
        self.config(command=self.active_work)
        self.bind('<1>',self.common_work)

    def active_work(self):
        pass

    def on_entering(self,event):
        self.config(bg='#EFEFEF')

    def on_leaving(self,event):
        self.config(bg='#FDFDFD')

    def common_work(self,event):
        self.parent.app.main.clearScreen()
        self.memory.shiftData(self.parent.activeTab,'Tab_in_front','Tabs_in_back')
        self.memory.shiftData(self,'Tabs_in_back','Tab_in_front')
        self.parent.reconfigure_tabs()


class GroupCenterTab(Tab):

    def __init__(self, parent):
        super().__init__(parent)
        self.memory.shiftData(self,'Tabs_in_back','Tab_in_front')


class TemporaryTab(Tab):

    def on_entering(self,event):
        if self.memory.getProcessData('Tab_in_front') == self:
            self.config(bg='firebrick1',fg='#FFFFFF')
        else:
            self.config(bg='#EFEFEF')

    def on_leaving(self,event):
        if self.memory.getProcessData('Tab_in_front') == self:
            self.config(bg='#EFEFEF',fg='#00AFE0')
        else:
            self.config(bg='#FDFDFD')

    def common_work(self,event):
        if self.memory.getProcessData('Tab_in_front') == self:
            self.destroy()
            self.memory['Tab_in_front'] = None
            self.parent.app.main.clearScreen()
        else:
            super().common_work(event)


class YearTab(Tab):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(text='Months')

    def active_work(self):
        self.parent.app.main.drawCalendar('yearly')


class MonthTab(GroupCenterTab):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(text=self.system.MONTHS[self.system.get_raw_date('month')-1].title())

    def active_work(self):
        self.parent.app.main.drawCalendar('monthly')


class TemporaryMonthTab(TemporaryTab):

    def __init__(self, parent, month):
        super().__init__(parent)
        self.config(text=month.title())
        self.month = month

    def active_work(self):
        self.parent.app.main.drawCalendar('monthly', self.month)


class TemporaryDayTab(TemporaryTab):

    def __init__(self, parent, date):
        super().__init__(parent)
        self.date = date
        self.config(text=f"{date[2]} {self.system.get_month_name(date[1])}")

    def active_work(self):
        self.parent.app.main.draw_card_holder(
            'events', self.system.get_date_from_tuple(self.date)
        )


class GCCardTab(GroupCenterTab):

    def __init__(self, parent):
        super().__init__(parent)
        self.date = self.system.get_raw_date('year','month','day')

    def active_work(self):
        self.parent.app.main.draw_card_holder(self['text'].lower(), self.date)


class RemindersTab(GCCardTab):

    def __init__(self, parent):
        super().__init__(parent)
        self.config(text='Reminders')


class ScheduleTab(GroupCenterTab):

    def __init__(self, parent):
        super().__init__(parent)
        self.config(text='Schedule')

    def active_work(self):
        self.parent.app.main.draw_schedule()


class NotesTab(GCCardTab):

    def __init__(self, parent):
        super().__init__(parent)
        self.config(text='Notes')


class ProfileTab(GroupCenterTab):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(text='My Profile')

    def active_work(self):
        self.parent.app.main.drawProfilePage()


class TabsFrame(MyFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(bg='#FEFEFE')
        self.config(width=self.parent.width, height=(6*self.parent.height/100))
        self.memory.addProcess('Tabs_in_back',[])
        self.memory.addProcess('Tab_in_front',None)

    @property
    def activeTab(self):
        return self.memory.getProcessData('Tab_in_front')

    def setTabs(self, opt_set='calendar'):
        if opt_set in ('calendar', 'profile', 'reminders', 'notes', 'schedule'):
            if opt_set == 'calendar':
                YearTab(self).grid(row=0, column=0, padx=(15, 0), pady=(5, 0))
                MonthTab(self).grid(row=0, column=1, pady=(5, 0))
            elif opt_set == 'profile':
                ProfileTab(self).grid(row=0, column=0, padx=(15, 0), pady=(5, 0))
            elif opt_set == 'reminders':
                RemindersTab(self).grid(row=0,column=0,padx=(15,0),pady=(5,0))
            elif opt_set == 'notes':
                NotesTab(self).grid(row=0,column=0,padx=(15,0),pady=(5,0))
            elif opt_set == 'schedule':
                ScheduleTab(self).grid(row=0,column=0,padx=(15,0),pady=(5,0))
            self.reconfigure_tabs()

    def clearTabs(self):
        for tab in self.winfo_children():
            tab.destroy()
        self.app.main.clearScreen()
        self.memory.clearProcess('Tab_in_front')
        self.memory.clearProcess('Tabs_in_back')

    def reconfigure_tabs(self):
        self.activeTab.active_work()
        self.activeTab.config(bg='#EFEFEF')
        if not isinstance(self.activeTab, TemporaryTab):
            self.activeTab.bind('<1>',lambda ev:None)
            self.activeTab.bind('<Enter>',lambda ev:None)
            self.activeTab.bind('<Leave>',lambda ev:None)
        for inactiveTab in self.memory.getProcessData('Tabs_in_back'):
            inactiveTab.config(bg='#FDFDFD')
            inactiveTab.bind('<1>',inactiveTab.common_work)
            inactiveTab.bind('<Enter>',inactiveTab.on_entering)
            inactiveTab.bind('<Leave>',inactiveTab.on_leaving)

    def add_month_tab(self, month):
        column = len(self.memory.getProcessData('Tabs_in_back')) + 1    # Plus one for the front tab in front
        if column <= 5:
            TemporaryMonthTab(self, month).grid(row=0, column=column, pady=(5,0))
        else:
            self.app.render_error_popup()

    def add_day_tab(self, date):
        column = len(self.memory.getProcessData('Tabs_in_back')) + 1
        if column <= 5:
            TemporaryDayTab(self, date).grid(row=0, column=column, pady=(5,0))
        else:
            self.app.render_error_popup()

# _________________________
