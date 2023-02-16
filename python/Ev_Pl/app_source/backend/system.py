# System object - Database and related

# _________________________________ Imports

import mysql.connector
from pickle import load,dump
import datetime as dt
from datetime import datetime as datim
from app_source.backend.memory import Memory
from app_source.backend.concepts import *

# _________________________________ Functions

# _________________________________ Objects

class System(object):

    MONTHS = ('jan', 'feb', 'march', 'april', 'may', 'june', 'july', 'aug', 'sep', 'oct', 'nov', 'dec')
    DAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

    def __init__(self,parent):
        self.parent = parent
        self.passFile = self.parent.passFile
        self.connected = False
        self.connection = None
        self.curs = None
        self.loggedIn = False
        self.current_user = 'Sys'
        self.sqlPasswd = None
        self.memory = Memory()

    @property
    def time_str(self):
        h = str(datim.now().time().hour).zfill(2)
        m = str(datim.now().time().minute).zfill(2)
        s = str(datim.now().time().second).zfill(2)
        return '%s : %s : %s' % (h, m, s)

    def get_month_name(self,month_int):
        return self.MONTHS[month_int-1].title()

    @staticmethod
    def get_raw_date(*args):
        return_var = []
        if 'year' in args:
            return_var.append(datim.now().date().year)
        if 'month' in args:
            return_var.append(datim.now().date().month)
        if 'day' in args:
            return_var.append(datim.now().date().day)
        if len(return_var) == 1:
            return return_var[0]
        else:
            return return_var

    @staticmethod
    def get_date_from_tuple(date_tuple):
        return dt.date(*date_tuple)
    
    @staticmethod
    def get_day_difference(origin_year=datim.now().date().year,
                           origin_month=datim.now().date().month,
                           origin_day=datim.now().date().day):
        current_date = datim.now().date()
        origin_date = dt.date(origin_year, origin_month, origin_day)
        return (origin_date - current_date).days

    @property
    def date_str(self):
        year = str(datim.now().date().year)
        month = self.get_month_name(datim.now().date().month)
        day = str(datim.now().date().day)
        return f'{month} {day}, {year}'

    def reset_system(self, caused_by_error=False):
        self.current_user = None
        self.loggedIn = False
        if caused_by_error is True:
            self.curs.execute('DROP DATABASE plan')
            self.parent.render_error_popup(text='Error occurred, restarting', restarter=True)
        self.resetMemory()

    def fetch_MySql_passwd(self):
        with open(self.passFile,'rb') as file:
            self.sqlPasswd = load(file)

    def write_pass(self, passwd):
        with open(self.passFile,'wb') as file:
            dump(passwd,file)

    def connect_to_MySQL(self):
        try:
            self.fetch_MySql_passwd()
            self.connection = mysql.connector.connect(host='localhost',user='root',passwd=self.sqlPasswd,charset='utf8')
            self.curs = self.connection.cursor()
            self.set_dBase()
        except mysql.connector.ProgrammingError:
            raise FileNotFoundError

    def set_dBase(self):
        try:
            self.curs.execute('USE plan')
            self.connected = True
        except mysql.connector.errors.ProgrammingError:
            self.create_dBase()

    def create_dBase(self):
        table_dict = {'users':(('F_Name','VARCHAR(10)'),('L_Name','VARCHAR(10)'),('DOB','DATE'),('Phone','Char(10)'),
                               ('U_Name','VARCHAR(10)','PRIMARY KEY'),('Passwd','VARCHAR(15)')),
                      'logs':(('Log_ID','INT','PRIMARY KEY','AUTO_INCREMENT'),('U_Name','VARCHAR(10)'),
                              ('Action','VARCHAR(15)'),('Log_DT','DATETIME')),
                      'events':(('Event_ID','INT','PRIMARY KEY','AUTO_INCREMENT'),('U_Name','VARCHAR(10)'),
                                ('Title','VARCHAR(15)'),('Description','VARCHAR(50)'),('Date','DATE')),
                      'tasks':(('Task_ID','INT','PRIMARY KEY','AUTO_INCREMENT'),('U_Name','VARCHAR(10)'),
                               ('Title','VARCHAR(15)'),('Description','VARCHAR(50)'),('Date', 'DATE'),
                               ('Daily', 'BOOL'),('Start','TIME'),('End','TIME'),('Priority', 'INT')),
                      'reminders':(('Rem_ID','INT','PRIMARY KEY','AUTO_INCREMENT'),('U_Name','VARCHAR(10)'),
                                   ('Title','VARCHAR(15)'),('Description','Varchar(50)'),('Rem_DT','DATETIME')),
                      'notes':(('Note_ID','INT','PRIMARY KEY','AUTO_INCREMENT'),('Title','VARCHAR(15)'),('Date','DATE'),
                               ('From_User','VARCHAR(10)'),('To_User','VARCHAR(10)'),('Note','VARCHAR(50)'))
                      }
        self.curs.execute('CREATE DATABASE plan')
        self.curs.execute('USE plan')
        for table in table_dict.keys():
            column_str_list = []
            for columnTup in table_dict[table]:
                column_str_list.append(str(' '.join(columnTup)))
            column_str = ','.join(column_str_list)
            self.curs.execute('CREATE TABLE %s (%s)' % (table,column_str))
        self.load_preset()
        self.connected = True

    def load_preset(self):
        user_null = "'System',NULL,NULL,NULL,'Sys',NULL"
        self.curs.execute('INSERT INTO users VALUES (%s)' % user_null)
        self.connection.commit()

    @staticmethod
    def checkFLDP(f, l, d, p):
        all_ok = True
        for i in (f,l,d,p):
            if i == '':
                all_ok = False
                break
        try:
            d_split = d.split('-')
            test_date = datim(int(d_split[0]),int(d_split[1]),int(d_split[2])).date()
            if test_date >= datim.now().date():
                raise ValueError
        except ValueError or TypeError:
            print(d)
            all_ok = False
        try:
            if len(str(p)) != 10:
                raise ValueError
            p = int(p)
        except ValueError:
            print(p)
            all_ok = False
        return all_ok

    @property
    def get_latestLog(self):
        self.curs.execute('SELECT Action FROM logs ORDER BY Log_ID DESC')
        actions = [action[0] for action in self.curs.fetchall()]
        try:
            return actions[0]
        except IndexError:
            return None

    @property
    def get_latestUser(self):
        self.curs.execute('SELECT U_Name FROM logs ORDER BY Log_ID DESC')
        user_list = [users[0] for users in self.curs.fetchall()]
        try:
            return user_list[0]
        except IndexError:
            return None

    @property
    def checkLogout(self):
        if self.get_latestLog in ('log_out',None):
            return True
        else:
            return False

    @property
    def accountsPresent(self):
        present = None
        self.curs.execute('SELECT U_Name FROM users')
        fetched_list = [uNameTup[0] for uNameTup in self.curs.fetchall()]
        if 'Sys' in fetched_list:
            if len(fetched_list) == 1:
                present = False
            elif (len(fetched_list) > 1) or (self.checkLogout is True):
                present = True
        else:
            self.reset_system(caused_by_error=True)
        print('present:', present)
        return present

    @property
    def openStartFrame(self):
        to_open = None
        self.curs.execute('SELECT U_Name FROM users')
        fetched_list = [uNameTup[0] for uNameTup in self.curs.fetchall()]
        if 'Sys' in fetched_list:
            if (len(fetched_list) != 2) or (self.checkLogout is True):
                to_open = True
            elif len(fetched_list) == 2:
                to_open = False
                self.current_user = self.get_latestUser
        else:
            self.reset_system(caused_by_error=True)
        print('to open:', to_open)
        return to_open

    @property
    def get_allUsers(self):
        self.curs.execute("SELECT U_Name FROM users WHERE U_Name != 'Sys'")
        users = [usersTup[0] for usersTup in self.curs.fetchall()]
        return users

    def addLog(self,action):
        self.curs.execute("INSERT INTO logs(U_Name,Action,Log_DT) VALUES('%s','%s','%s')" % (self.current_user, action,
                                                                                             datim.now()))
        self.connection.commit()

    def checkUname(self, u, for_login=False):
        all_ok = True
        self.curs.execute('SELECT U_Name FROM users')
        fetched_list = self.curs.fetchall()
        if (u == '') or (u == 'Sys'):
            all_ok = False
        else:
            presence_bool = (u in (userTup[0] for userTup in fetched_list))
            if for_login is True:
                all_ok = presence_bool
            elif for_login is False:
                all_ok = not presence_bool
        return all_ok

    def matchUP(self,u,p):
        match = True
        if self.checkUname(u, for_login=True) is False:
            match = False
        else:
            self.curs.execute("SELECT passwd FROM users WHERE U_Name = '%s'" % u)
            fetched_list = self.curs.fetchall()
            if p != (fetched_list[0])[0]:
                match = False
        return match

    def addAcc(self):
        acc_data = self.memory.getProcessData('Creating Account')
        self.memory.removeProcess('Creating Account')
        f = acc_data[0]
        l = acc_data[1]
        dob = acc_data[2]
        phone = acc_data[3]
        u = acc_data[4]
        passwd = acc_data[5]
        self.curs.execute("INSERT INTO users VALUES ('%s','%s','%s','%s','%s','%s')" % (f,l,dob,phone,u,passwd))
        self.connection.commit()
        self.current_user = u
        self.addLog('log_in')

    def delCurrUser(self):
        self.curs.execute(f"DELETE FROM users WHERE U_Name = '{self.current_user}'")
        self.connection.commit()

    @property
    def account_details(self):
        self.curs.execute(f"SELECT F_Name,L_Name,DOB,Phone FROM users WHERE U_Name = '{self.current_user}'")
        fetched_list = (self.curs.fetchall())[0]
        f = fetched_list[0]
        l = fetched_list[1]
        dob_list = [int(num_str) for num_str in str(fetched_list[2]).split('-')]
        dob = f'{self.get_month_name(dob_list[1])} {dob_list[2]}, {dob_list[0]}'
        age = self.get_age(dob_list[0],dob_list[1],dob_list[2])
        phone = fetched_list[3]
        return tuple((f'{f} {l}',dob,age,phone))

    @staticmethod
    def get_age(dob_year, dob_month, dob_day):
        current_year = datim.now().date().year
        year_diff = (current_year-dob_year)
        if datim(current_year,dob_month,dob_day).date() < datim.now().date():
            return str(year_diff)
        else:
            return str(year_diff-1)

    def resetMemory(self):
        self.memory = Memory()

    def get_card_values(self, card_type, date=datim.now().date()):
        if card_type in ('events', 'tasks'):
            self.curs.execute(
                f"SELECT * FROM {card_type} WHERE U_Name = '{self.current_user}'"
                + f"and Date = '{date}'"
            )
        else:
            self.parent.render_error_popup('Not Implemented')
        fetched_list = self.curs.fetchall()
        return [Task.from_tuple(value_tuple) for value_tuple in fetched_list]

    def create_card(self, card_type, *card_value_sets, forced_card=None):
        if card_type == 'event':
            event = Event(*card_value_sets)
            if event.event_visibility == 'self':
                user = self.current_user
            else:
                user = 'Sys'
            self.curs.execute(
                f"INSERT INTO events(U_Name, Title, Description, Date) VALUES"
                + f"('{user}','{event.event_name}','{event.event_desc}','{event.event_date}')"
            )
            if event.task_bool is True:
                self.create_card('task', forced_card=Task.from_event_values(*card_value_sets))
        elif card_type == 'task':
            task = Task(*card_value_sets) if forced_card is None else forced_card
            if task.repeat is True:
                date_col, date_entry, daily = '', '', True
            else:
                date_col, date_entry, daily = ', Date', f",'{task.date}'", False
            self.curs.execute(
                f"INSERT INTO tasks(U_Name, Title, Description, Daily, Start, End, Priority{date_col}) VALUES"
                + f"('{self.current_user}','{task.task_name}','{task.task_desc}',{daily},"
                + f"'{task.start}','{task.end}',{task.priority}{date_entry})"
            )
        elif card_type == 'reminder':
            ...
        elif card_type == 'note':
            ...
        self.connection.commit()

# ___________________________________
