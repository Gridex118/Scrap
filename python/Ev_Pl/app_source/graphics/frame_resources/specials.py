# Graphics for Event Planner - Specials(Padding, Calendar)

# _____________________ Imports

from tkinter import Frame, Label
from calendar import mdays, weekday

# ______________________ Functions

# _____________________ Classes

class Padframe(Frame):

    def __init__(self,parent,bg='#FDFDFD',width=200,height=135):
        super().__init__(parent)
        self.config(bg=bg,width=width,height=height)
        self.grid_propagate(0)


class DragRegion(Frame):

    def __init__(self, parent, target, width, height, free_axis='xy'):
        super().__init__(parent)
        self.target = target
        self.config(bg=parent['bg'], width=width, height=height)
        self.grid_propagate(False)
        self.free_axis = free_axis
        self.move = False
        self.origin = [0,0]
        self.bind('<1>', self.button_one_event)
        self.bind('<Motion>', self.move_root)
        self.bind('<ButtonRelease-1>', lambda ev: self.stop_root_movement())

    def move_root(self, event):
        if self.move:
            if 'x' in self.free_axis:
                self.target.x_corr = int(self.target.x_corr + (event.x - self.origin[0]))
            if 'y' in self.free_axis:
                self.target.y_corr = int(self.target.y_corr + (event.y - self.origin[1]))
            new_geometry = self.geo_str(
                self.target.width, self.target.height,
                self.target.x_corr, self.target.y_corr
            )
            self.target.geometry(new_geometry)

    def button_one_event(self, event):
        self.move = True
        self.origin = [event.x, event.y]

    def stop_root_movement(self):
        self.move = False

    @staticmethod
    def geo_str(width, height, x, y):
        return f'{width}x{height}+{x}+{y}'


class TitleBarMultiButton(DragRegion):

    def __init__(self, parent, restrict_minimization):
        super(DragRegion, self).__init__(parent)
        self.target = parent.app
        self.free_axis = 'xy'
        self.restrict_minimization = restrict_minimization
        self.move = False
        self.origin = [0, 0]
        self.config(bg='#10E0DA', width=100, height=10)
        self.grid_propagate(0)
        self.bind('<Enter>', lambda ev: self.enter_color())
        self.bind('<Control-Enter>', lambda ev: self.enter_color('ctrl'))
        self.bind('<Alt-Enter>', lambda ev: self.enter_color('alt'))
        self.bind('<Leave>', lambda ev: self.config(bg='#10E0DA'))
        self.bind('<1>', self.button_one_event)
        self.bind('<Control-1>', lambda ev: self.button_one_event(ev, 'ctrl'))
        self.bind('<Alt-1>', lambda ev: self.button_one_event(ev, 'alt'))
        self.bind('<Motion>', self.move_root)
        self.bind('<ButtonRelease-1>', lambda ev: self.stop_root_movement())

    def button_one_event(self, event, modifier=None):
        self.enter_color(modifier=modifier)
        if (modifier == 'ctrl') and (not self.restrict_minimization):
            self.target.minimize()
        elif modifier == 'alt':
            super().button_one_event(event)
        else:
            self.target.shutdown()

    def enter_color(self, modifier=None):
        if (modifier == 'ctrl') and (not self.restrict_minimization):
            color = '#00D0EF'
        elif modifier == 'alt':
            color = '#EAD010'
        else:
            color = '#FF5A5A'
        self.config(bg=color)


class TitleBar(Frame):

    def __init__(self, parent, restrict_minimization=False):
        super().__init__(parent)
        self.app = parent
        self.memory = self.app.system.memory
        self.config(
            bg='#FEFEFE',
            width=parent.width,
            height=10
        )
        self.grid_propagate(False)
        self.multi_button = TitleBarMultiButton(self, restrict_minimization)
        self.multi_button_x_pos = (self['width'] - self.multi_button['width'])/2
        self.multi_button.place(x=self.multi_button_x_pos, y=0)


class ContentHolder(Frame):

    def __init__(self, parent, width, height, bg, content_object, content_values):
        super().__init__(parent, width=width, height=height, bg=bg)
        self.grid_propagate(False)


class ContentBook(Frame):

    def __init__(self, parent, width, height, content_object, content_values):
        super().__init__(parent)
        self.config(width=width, height=height, bg='#FAFAFA')
        self.grid_propagate(False)
        self.content_holder = ContentHolder(
            self, (width-20), height, parent['bg'], content_object, content_values
        )
        self.content_holder.grid(row=0, column=1)
        self.left_arrow = Frame(self, width=10, height=height, bg=self['bg'])
        self.right_arrow = Frame(self, width=10, height=height, bg=self['bg'])
        for arrow in (self.left_arrow,self.right_arrow):
            arrow.grid_propagate(False)
            arrow.bind('<Enter>', self.on_entering_arrow)
            arrow.bind('<Leave>', self.on_leaving_arrow)
        self.left_arrow.grid(row=0, column=0)
        self.right_arrow.grid(row=0, column=2)

    def on_entering_arrow(self, event):
        event.widget.config(bg='#DEDEDE')

    def on_leaving_arrow(self, event):
        event.widget.config(bg=self['bg'])


class Calendar(Frame):

    def __init__(self,parent,calendar, month='current'):
        super().__init__(parent)
        self.parent = parent
        self.system = self.parent.system
        self.app = self.parent.app
        self.config(bg='#EFEFEF')
        self.config(width=self.parent['width'],height=self.parent['height'])
        self.grid_propagate(0)
        self.tile_x = 0
        self.tile_y = 0
        if calendar == 'yearly':
            self.tile_x,self.tile_y = CalendarTile.calculate_side(parent=self, row_count=3,
                                                                  column_count=4)
            month_index = 0
            for row in range(3):
                for column in range(4):
                    month_str = self.system.MONTHS[month_index].title()
                    CalendarTile(self, month_str,(self.tile_x, self.tile_y), 'month').grid(
                        row=row, column=column
                        )
                    month_index += 1
        elif calendar == 'monthly':
            self.tile_x,self.tile_y = CalendarTile.calculate_side(parent=self, row_count=5, column_count=7)
            if month == 'current':
                month_number = self.system.get_raw_date('month')
            else:
                month_number = self.system.MONTHS.index(month) + 1
            total_day_count = mdays[month_number]
            row = 0
            column = 0
            for day in range(1, total_day_count+1):
                if month == 'current':
                    day_str = f"{day}\n{self.system.DAYS[weekday(*self.system.get_raw_date('year','month'), day)]}"
                else:
                    day_str = f"{day}\n{self.system.DAYS[weekday(self.system.get_raw_date('year'),month_number,day)]}"
                date = (self.system.get_raw_date('year'), month_number, day)
                CalendarTile(self, day_str, (self.tile_x, self.tile_y), 'day', date).grid(
                    row=row, column=column
                    )
                column += 1
                if column == 7:
                    column = 0
                    row += 1


class CalendarTile(Frame):

    def __init__(self,parent,text,side,tile_type, date=None):
        super().__init__(parent)
        self.parent = parent
        self.tile_type = tile_type
        self.date = date
        self.text = text
        self.side_x = side[0]
        self.side_y = side[1]
        self.config(bg='#FDFDFD')
        self.config(width=self.side_x,height=self.side_y)
        self.grid_propagate(0)
        self.font = ('Sans Serif',16,'italic')
        self.label = Label(self,text=text,bg='#FDFDFD',fg='#00AFE0',font=self.font)
        self.label.grid(row=0,column=0,padx=((self['width']/2-35),0),pady=((self['height']/2-30),0))
        self.bind('<Enter>', lambda ev: self.on_entering())
        self.bind('<Leave>', lambda ev: self.on_leaving())
        for widget in (self, self.label):
            widget.bind('<1>', lambda ev: self.action())

    def action(self):
        if self.tile_type == 'month':
            self.parent.app.tabs.add_month_tab(self.text.lower())
        else:
            self.parent.app.tabs.add_day_tab(self.date)

    @staticmethod
    def calculate_side(parent, row_count, column_count):
        base_x = parent['width']
        base_y = parent['height']
        tile_x = base_x/column_count
        tile_y = base_y/row_count
        return tile_x,tile_y

    def on_entering(self):
        self.config(bg='#EFEFEF')
        self.config(highlightthickness=10,highlightbackground='#FFFFFF')
        self.label.config(bg='#EFEFEF')

    def on_leaving(self):
        self.config(bg='#FDFDFD')
        self.config(highlightthickness=0)
        self.label.config(bg='#FDFDFD')


class Card(Frame):

    def __init__(self, parent, card_info):
        super().__init__(parent)
        self.parent = parent
        self.index = 0
        self.config(
            bg='#FAFAFA',
            width=(self.parent['width']*4/5),
            height=(self.parent['height']*85/100)
        )
        self.grid_propagate(0)

# ____________________
