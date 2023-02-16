# Graphics for Event Planner - (Labels, Entry Boxes)

# _____________________________ Imports

from tkinter import Entry, Frame,StringVar, Label

# _____________________________ Objects

class MyLabel(Label):

    font_styles = {'alpha': ('Sans Serif', 'italic')}

    def __init__(self, parent, text, font_style='alpha', size=12, color='black'):
        super().__init__(parent, text=text, bg=parent['bg'], fg=color)
        self.font_style = font_style
        self.font_size = size
        self.config(font=self.font_style_tuple)

    @property
    def font_style_tuple(self):
        style = self.font_styles[self.font_style]
        return tuple((style[0], self.font_size, style[1]))


class MyEntry(Entry):

    def __init__(self, parent, header, width, bg='parental'):
        super().__init__(parent)
        self.parent = parent
        self.app = self.parent.app
        self.header = header
        self.config(width=width)
        if bg == 'parental':
            box_background = parent['bg']
        else:
            box_background = bg
        self.config(bg=box_background,relief='flat')
        self.font = ('Comic Sans',13,'italic')
        self.text_var = StringVar(self, self.header)
        self.config(fg='gray45',font=self.font)
        self.grid_propagate(0)
        self.config(textvar=self.text_var)
        self.change_text()

    def change_text(self):
        if self.app.focus_get() == self:
            if self.text_var.get() == self.header:
                self.text_var.set('')
        else:
            if self.text_var.get() == '':
                self.text_var.set(self.header)
        self.after(85, self.change_text)


class TextEntry(Frame):

    def __init__(self, parent, header, default='', width=500, height=30, entry_width=30):
        super().__init__(parent)
        self.parent = parent
        self.app = self.parent.app
        self.system = self.parent.app
        self.header = header
        self.default = default
        self.config(bg='#F5F5F5')
        self.config(width=width,height=height)
        self.grid_propagate(0)
        self.entry = MyEntry(self, self.header, entry_width)
        self.entry.grid(row=0,column=0,padx=(15,0),pady=(5,0))
        self.bind('<1>', lambda ev: self.focus_on_entry())

    def focus_on_entry(self):
        self.entry.focus()

    def get(self):
        text = self.entry.get()
        if text == self.header:
            return self.default
        else:
            return text


class SpecialEntry(Frame):

    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.app = self.parent.app
        self.system = self.parent.system
        self.config(bg=parent['bg'])


class DateEntry(SpecialEntry):

    def __init__(self,parent):
        super().__init__(parent)
        self.year = MyEntry(self, 'YYYY', 15, '#F5F5F5')
        self.month = MyEntry(self, 'MM', 10, '#F5F5F5')
        self.day = MyEntry(self, 'DD', 10, '#F5F5F5')
        self.year.grid(row=0,column=0)
        self.month.grid(row=0,column=1,padx=(10,0))
        self.day.grid(row=0,column=2,padx=(7,0))

    def get(self):
        date = '-'.join([str(self.year.get()),str(self.month.get()),str(self.day.get())])
        return date


class TimeEntry(SpecialEntry):

    def __init__(self, parent):
        super().__init__(parent)
        self.hour = MyEntry(self, 'Hour', 10, '#F5F5F5')
        self.minute = MyEntry(self, 'Minute', 10, '#F5F5F5')
        self.hour.grid(row=0, column=0)
        self.minute.grid(row=0, column=1, padx=(7,0))

    def get(self):
        return f"{self.hour.get()}:{self.minute.get()}:00"

# _______________________________
