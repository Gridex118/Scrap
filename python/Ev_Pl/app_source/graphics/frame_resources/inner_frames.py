# Inner Frames - Graphics for Event Planner

# __________________ Imports

from app_source.graphics.frame_resources.bases import MyFrame, TitledFrame, ActiveFrame
from app_source.graphics.frame_resources.specials import *
from app_source.graphics.frame_resources.buttons import *
from app_source.graphics.frame_resources.text import *

# __________________ Classes

class StartMenuFrame(MyFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(bg='#FFFFFF')
        self.config(width=(3*self.parent['width']/5),height=(3*self.parent['height']/5))
        self.frame = None
        present = self.system.accountsPresent
        if present is True:
            self.loginSeq()
        elif present is False:
            self.registSeq()

    def setFrame(self):
        self.frame.grid(row=0,column=0,padx=(self['width']/20,0),pady=(self['height']/20,0))

    def registSeq(self):
        self.frame = CrAccFrameOne(self)
        self.setFrame()

    def loginSeq(self):
        self.frame = LoginFrame(self)
        self.setFrame()

    def altFrameP2(self):
        self.frame.destroy()
        self.frame = CrAccFrameTwo(self)
        self.setFrame()

    def altFrameCr(self):
        self.frame.destroy()
        self.registSeq()

    def altFrameLogin(self):
        self.frame.destroy()
        self.loginSeq()

    def endStartFrame(self,login=False,register=False):
        try:
            self.frame.destroy()
        except AttributeError:
            pass
        if (login is True) or (register is True):
            if register is True:
                self.system.addAcc()
            elif login is True:
                self.system.addLog('log_in')
            self.app.login()
            self.destroy()


class CrAccFrameOne(MyFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(bg=parent['bg'])
        self.config(width=(9*self.parent['width']/10),height=(9*self.parent['height']/10))
        self.lFont = ('Ariel',12,'bold')
        self.first_name = TextEntry(self, 'First Name', width=250)
        self.first_name.grid(row=0, column=0, padx=(0, 5), pady=(self['height'] / 5, 0))
        self.last_name = TextEntry(self, 'Last Name', width=250)
        self.last_name.grid(row=0, column=1, pady=(self['height'] / 5, 0))
        label = Label(self,text='DOB: ', bg=self['bg'], fg='#00AFE0', font=self.lFont)
        label.grid(row=1, column=0, columnspan=2, pady=(10,0), sticky='w')
        self.date = DateEntry(self)
        self.date.grid(row=1, column=0, columnspan=3, pady=(10, 0))
        self.phone = TextEntry(self, 'Phone Number', width=350)
        self.phone.grid(row=2, column=0, columnspan=3, pady=(10, 0), sticky='w')
        AccNextButton(self).grid(
            row=0, rowspan=4, column=0, columnspan=4,
            pady=(280,0), padx=(7*self['width']/10,0)
        )

    def nextPage(self):
        f = str(self.first_name.get())
        l = str(self.last_name.get())
        d = str(self.date.get())
        p = str(self.phone.get())
        if self.system.checkFLDP(f,l,d,p) is True:
            self.parent.altFrameP2()
            self.memory.addProcess('Creating Account',[f,l,d,p])
        else:
            self.app.render_error_popup('Error, Please recheck your input')


class CrAccFrameTwo(MyFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(bg=parent['bg'])
        self.config(width=(9*self.parent['width']/10),
                    height=(9*self.parent['height']/10))
        self.user_name = TextEntry(self, 'Username')
        self.user_name.grid(row=0, column=1, sticky='w',
                            pady=(self['height'] / 5, 0))
        self.password = TextEntry(self, 'Password')
        self.password.grid(row=1, column=1, sticky='w', pady=(20, 0))
        AccFinishButton(self).grid(
            row=0, rowspan=3, column=0,
            columnspan=2, pady=(280, 0),
            padx=(7 * self['width'] / 10, 0)
        )

    def register(self):
        u = str(self.user_name.get())
        p = str(self.password.get())
        cond1 = len(p) in range(1,16)
        cond2 = p.isalnum()
        cond3 = self.system.checkUname(u)
        if cond1 and cond2 and cond3:
            self.memory.updateProcessData('Creating Account',[u,p])
            self.parent.endStartFrame(register=True)
        else:
            self.app.render_error_popup('Error, Please check your input')


class LoginFrame(MyFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(bg=parent['bg'])
        self.config(width=(9*self.parent['width']/10),
                    height=(9*self.parent['height']/10))
        self.u = TextEntry(self, 'Username')
        self.u.grid(row=0, column=1, sticky='w', pady=(self['height'] / 5, 0))
        self.p = TextEntry(self, 'Password')
        self.p.grid(row=1, column=1, sticky='w', pady=(20, 0))
        LoginButton(self).grid(
            row=0, rowspan=3, column=0, columnspan=2, pady=(270,0),padx=(7*self['width']/10,0)
        )
        CreateAccButton(self).grid(
            row=0, rowspan=3, column=1, sticky='w', columnspan=2, pady=(270, 0)
        )
        for t_box in (self.u, self.p):
            t_box.entry.bind('<Return>', lambda e: self.login())

    def login(self):
        u = str(self.u.get())
        p = str(self.p.get())
        if self.system.matchUP(u,p) is True:
            self.system.current_user = u
            self.parent.endStartFrame(login=True)
        else:
            self.app.render_error_popup('Invalid Login Credentials')

    def crAcc(self):
        self.parent.altFrameCr()


class CalenFrame(ActiveFrame):

    def __init__(self,parent,calendar='monthly',month='current'):
        super().__init__(parent)
        self.calendar = calendar
        self.month = month
        self.setCalendar()

    def setCalendar(self):
        if self.calendar == 'monthly':
            self.drawMonthlyCalen()
        elif self.calendar == 'yearly':
            self.drawYearlyCalen()

    def drawMonthlyCalen(self):
        Calendar(self, 'monthly', self.month).grid(row=0, column=0)

    def drawYearlyCalen(self):
        Calendar(self,'yearly').grid(row=0, column=0)


class CardHoldingFrame(ActiveFrame):

    def __init__(self, parent, card_type, date):
        super().__init__(parent)
        self.cards = self.system.get_card_values(card_type, date)
        self.current_card = Card(self, self.cards)
        SpecificCardButton(self, 'Edit').grid(row=0,column=0,pady=(10,0),padx=(120,0))
        SpecificCardButton(self, 'Delete').grid(row=0,column=1,pady=(10,0))
        self.current_card.grid(row=1,column=0, padx=(100,0), pady=(10,0), columnspan=3)
        CardButton(self, 'Prev').grid(row=2,column=0,padx=(120,0),pady=(5,0))
        CardButton(self, 'Add', card_type).grid(row=2, column=1,sticky='W',padx=(20,0),pady=(5,0))
        CardButton(self, 'Next').grid(row=2, column=2,sticky='W',pady=(5,0))


class ScheduleFrame(ActiveFrame):

    def __init__(self, parent):
        super().__init__(parent)
        TimeTableFrame(self).grid(row=0, column=0, padx=(5,0), pady=(5,0), rowspan=2)
        FreeTimeFrame(self).grid(row=0, column=1, padx=(5,0), pady=(5,0))
        TTToolsFrame(self).grid(row=1, column=1, padx=(5,0), pady=(5,0))


class TimeTableFrame(TitledFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            width=((parent['width']/2)-10),
            height=(parent['height']-10),
            text='Time Table'
        )
        tasks = self.system.get_card_values('tasks')
        ContentBook(self, (self['width']-10), (self['height']-10), None, tasks)


class FreeTimeFrame(TitledFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            width=((parent['width']/2)-10),
            height=((parent['height']*3/5)-10),
            text='Free Time'
        )


class TTToolsFrame(TitledFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            width=((parent['width']/2)-10),
            height=((parent['height']*2/5)-10),
            text='Time Table Tools'
        )


class ProfileFrame(ActiveFrame):

    def __init__(self,parent):
        super().__init__(parent)
        DeleteAccButton(self).grid(row=0, column=0, padx=((self['width'] - 200), 0))
        UserDetailsFrame(self).grid(row=1, column=0, pady=(10, 0))
        LogoutButton(self).grid(row=2, column=0, pady=(20, 0), padx=((self['width'] - 200), 0))

    def logout(self):
        self.system.addLog(action='log_out')
        self.app.restart_app()

    def deleteAccount(self):
        self.system.delCurrUser()
        self.logout()


class UserDetailsFrame(MyFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(bg='#EFEFEF')
        self.config(width=self.parent['width'],height=(4*self.parent['height']/5))
        BioFrame(self).grid(row=0, column=0)


class BioFrame(MyFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(bg='#FFFFFF')
        self.config(width=(7*self.parent['width']/20),height=self.parent['height'])
        self.fnFont = ('Caliberi',16,'bold','italic')
        self.fvFont = ('Sans Serif',14,'italic')
        self.details = self.system.account_details
        self.setLabel(text='User Name: ',font=self.fnFont,row=0,column=0,pady=(50,0))
        self.setLabel(text=self.system.current_user, font=self.fvFont, row=0, column=1, pady=(50, 0))
        self.setLabel(text='Name: ',font=self.fnFont,row=1,column=0,pady=(20,0))
        self.setLabel(text=self.details[0],font=self.fvFont,row=1,column=1,pady=(20,0))
        self.setLabel(text='Date of Birth: ',font=self.fnFont,row=2,column=0,pady=(20,0))
        self.setLabel(text=self.details[1],font=self.fvFont,row=2,column=1,pady=(20,0))
        self.setLabel(text='Age: ',font=self.fnFont,row=3,column=0,pady=(20,0))
        self.setLabel(text=self.details[2],font=self.fvFont,row=3,column=1)
        self.setLabel(text='Phone No: ',font=self.fnFont,row=4,column=0,pady=(20,0))
        self.setLabel(text=self.details[3],font=self.fvFont,row=4,column=1,pady=(20,0))
        UpdateAccButton(self).grid(row=5, column=0, columnspan=2, padx=(20, 0), pady=(120, 0), sticky='w')

    def setLabel(self,text,font,row,column,padx=(15,0),pady=(10,0),sticky='w'):
        label = Label(self,text=text,bg=self['bg'],fg='#00AFE0',font=font)
        label.grid(row=row,column=column,padx=padx,pady=pady,sticky=sticky)

# __________________________
