# Right Frame - Graphics for Event Planner

# ___________________ Imports

from tkinter import Label
from app_source.graphics.nav_bar import *

# ___________________ Classes

class Rightframe(MyFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(bg='#FCFCFC')
        self.config(width=(self.parent.width/5),height=((941*self.parent.height/1000) - 10))
        self.nav = NavBar(self)
        self.nav.grid(row=0,column=0)
        Datetimeframe(self).grid(row=1,column=0,pady=(20,0))


class Datetimeframe(MyFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(bg='#F5F5F5')
        self.config(width=self.parent['width'],height=(self.parent['height']/5))
        self.dFontTup = ('Ariel',17,'italic')
        self.tFontTup = ('Ariel',14,'bold')
        self.dLbl = Label(self,bg=self['bg'],font=self.dFontTup,fg='#00AFE0')
        self.tLbl = Label(self,bg=self['bg'],font=self.tFontTup,fg='#00AFE0')
        self.dLbl.grid(row=0,column=0,padx=(self['width']/3,0),pady=(self['height']/5,0))
        self.tLbl.grid(row=1,column=0,padx=(2*self['width']/5,0))
        self.updateDT()

    def updateDT(self):
        self.dLbl.config(text=self.system.date_str)
        self.tLbl.config(text=self.system.time_str)
        self.after(100, self.updateDT)

# _________________________________________
