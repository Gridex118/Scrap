# Event Planner Graphics Bases

# ________________ Imports

from tkinter import Frame, Button, Label

# ________________ Classes

class MyLesserFrame(Frame):

    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.system = self.parent.system
        self.memory = self.system.memory
        self.grid_propagate(0)
        self.bind('<1>',lambda ev: self.divertFocus())

    def divertFocus(self):
        self.focus()


class MyFrame(MyLesserFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.app = self.parent.app


class ActiveFrame(MyFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(bg='#EDEDED')
        self.config(width=(99*parent['width']/100),height=(99*parent['height']/100))


class TitledFrame(MyFrame):

    def __init__(self, parent, width, height, text='title'):
        super().__init__(parent)
        self.config(bg='#FDFDFD', width=width, height=height)
        self.top_bar = MyFrame(self)
        self.top_bar.config(bg='#DEDEDE', width=self['width'],
                            height=30)
        self.title_font = ('Comic Sans', 16, 'italic')
        self.title = Label(
            self.top_bar, text=text,
            bg=self.top_bar['bg'],
            font=self.title_font,
            fg='#FFFFFF'
            )
        self.title.grid(padx=(20,0))
        self.top_bar.grid(row=0, column=0, columnspan=4)


class MyButton(Button):

    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.system = self.parent.system
        self.memory = self.system.memory
        self.config(bg='#FAFAFA',fg='#00AFE0',
                    activebackground='#109FFF',
                    activeforeground='#FEFEFE',
                    relief='flat')
        self.config(width=14,height=1)
        self.config(font=('Ariel',10,'bold','italic'))
        self.grid_propagate(0)
        self.bind('<Enter>',self.on_entering)
        self.bind('<Leave>',self.on_leaving)

    def on_entering(self,event):
        self.config(bg='#109FFF',fg='#FEFEFE')

    def on_leaving(self,event):
        self.config(bg='#FAFAFA',fg='#00AFE0')


class MyBlueButton(MyButton):

    def __init__(self, parent):
        super().__init__(parent)
        self.config(
            bg='#00AFE0',
            fg='#FAFAFA',
            activebackground='#00E0AF'
            )

    def on_entering(self,event):
        self.config(bg='#00E0AF')

    def on_leaving(self,event):
        self.config(bg='#00AFE0')

# ____________________________
