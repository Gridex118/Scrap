# Main Frame - Graphics for Event Planner

# _____________________ Imports

from app_source.graphics.frame_resources.bases import MyFrame
import app_source.graphics.frame_resources.inner_frames as inner

# _____________________ Classes

class Mainframe(MyFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.config(bg='#EFEFEF')
        self.config(width=(799*self.parent.width/1000),height=((937*self.parent.height/1000) - 10))

    def drawStartFrame(self):
        to_open = self.system.openStartFrame
        if to_open is True:
            inner.StartMenuFrame(self).grid(row=0, column=0, padx=(self['width'] / 5, 0), pady=(self['height'] / 5, 0))
        elif to_open is False:
            self.parent.login()

    def place_sub_frame(self, frame):
        frame.grid(
            row=0, column=0,
            padx=((self['width']/200),0),
            pady=((self['height']/200),0)
            )

    def drawCalendar(self,calendar='monthly', month='current'):
        self.clearScreen()
        self.place_sub_frame(
            inner.CalenFrame(self, calendar=calendar, month=month)
            )

    def drawProfilePage(self):
        self.clearScreen()
        self.place_sub_frame(inner.ProfileFrame(self))

    def draw_card_holder(self, card_type, date):
        self.clearScreen()
        self.place_sub_frame(
            inner.CardHoldingFrame(self, card_type, date)
            )

    def draw_schedule(self):
        self.clearScreen()
        self.place_sub_frame(inner.ScheduleFrame(self))

    def clearScreen(self):
        for widget in self.winfo_children():
            widget.destroy()


# _______________________
