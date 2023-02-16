# Event Planner Main Window

# __________________________________________________Imports

from tkinter import Tk
from threading import Thread
from app_source.graphics import *
from app_source.backend.system import System

# __________________________________________________ Objects

class App(Tk):

    def __init__(self,pass_file):
        super().__init__()
        self.state('withdrawn')
        self.passFile = pass_file
        self.app = self
        self.system = System(self)
        self.running = True
        self.load_screen = LoadScreen(self)
        self.width = 1216
        self.height = 622
        self.x_corr = (self.winfo_screenwidth()-self.width)/2
        self.y_corr = (((self.winfo_screenheight()-self.height)/2)-30)
        self.geometry('%dx%d+%d+%d' % (self.width,self.height,self.x_corr,self.y_corr))
        self.overrideredirect(True)
        self.config(bg='firebrick1')
        self.wm_attributes('-alpha', 0.985)
        self.wm_attributes('-topmost', True)
        Thread(target=self.load_screen.wait).start()
        self.start_connection_thread()
        
    def __str__(self):
        return 'Scheduling software'

    def minimize(self):
        Floater(self)
        self.state('withdrawn')

    def maximize(self, floater):
        floater.destroy()
        self.state('normal')

    def start_connection_thread(self):
        Thread(target=self.connectSQL).start()

    def connectSQL(self):
        sleep(0.5)
        try:
            self.system.connect_to_MySQL()
        except FileNotFoundError:
            self.displayPassPrompt()

    def displayPassPrompt(self):
        SqlPassPop(self, self.load_screen)

    def feed_passwd_to_sys(self, passwd):
        self.system.write_pass(passwd)
        self.start_connection_thread()
        
    def draw_frames(self):
        self.t_bar = TitleBar(self)
        self.t_bar.place(x=0, y=0)
        self.tabs = TabsFrame(self)
        self.tabs.place(x=0, y=10)
        self.right = Rightframe(self)
        self.right.place(x=977, y=47)
        self.main = Mainframe(self)
        self.main.place(x=5,y=47)
        self.main.drawStartFrame()

    def restart_app(self):
        self.state('withdrawn')
        self.system.reset_system()
        Thread(target=self.restart_app_thread).start()

    def restart_app_thread(self):
        sleep(1)
        self.config(bg='firebrick1')
        for frame in self.winfo_children():
            frame.destroy()
        self.draw_frames()
        self.state('normal')

    def login(self):
        self.system.loggedIn = True
        self.config(bg='sky blue')
        self.right.nav.setButtons()

    def shutdown(self):
        self.running = False
        self.destroy()

    def render_error_popup(self, text='', restarter=False):
        pop = ErrorPopUp(self, text=text)
        if restarter is True:
            pop.buttonConfig(command=self.restart_app)

    def render_card_editor(self, card_type='events'):
        CardEditor(self, card_type)

# __________________________________
