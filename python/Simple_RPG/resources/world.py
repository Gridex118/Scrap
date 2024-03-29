# World object - Main object
#______ Imports and related

from creature import *
from skills import Skill
from items import *
from spec_functions import *
from misc_functions import *
from systems import *
from random import randint,shuffle
from time import time as t


#______ Objects

class World(object):

    def com_seq(self,state):
        return get_com(state)


class SubWorld(World):

    def __init__(self,parent):
        self.parent = parent

    def com_seq(self,state):
        return super().com_seq(state)


class Dungeon(SubWorld):

    def __init__(self,parent):
        super().__init__(parent)
        self.currentFloor = 1

    def get_stairsFound(self):
        if self.currentFloor < self.parent.maxFloor:
            return True
        else:
            return False

    def resetFloor(self):
        self.currentFloor = 1

    def com_seq(self):
        print()
        com = super().com_seq(state='dungeon')
        if com == 'explore':
            self.explore()
        elif com == 'save':
            self.parent.saveState()
        elif com == 'status':
            self.parent.player.status()
        elif com == 'return to town':
            sprint('You have moved back to the Town')
            self.resetFloor()
        elif com == 'inventory':
            self.parent.player.items()
        elif com == 'equipment':
            self.parent.player.equipment()
            print()
            self.parent.msSys.equip()
        elif com == 'go to next floor':
            flrBoss = {23:'ogre',35:'ghoul',100:'devil'}
            if self.currentFloor == 100:
                sprint('You have reached the highest floor.')
            elif self.currentFloor in flrBoss.keys() and \
                    self.parent.bDef[flrBoss[self.currentFloor]] == False:
                        sprint('You must defeat the floor boss first.')
            elif self.get_stairsFound() == False:
                sprint('You are yet to find the stairs.')
            elif self.get_stairsFound():
                sprint('You went to the next floor.')
                self.currentFloor += 1
                sprint('Current floor: %d'%self.currentFloor)
        if com != 'return to town':
            self.com_seq()

    def get_monList(self):
        l = []
        if self.currentFloor >= 1:
            l.extend(['slime','goblin'])
        if self.currentFloor >= 3:
            l.append('orc')
        if self.currentFloor >= 10:
            l = (['sp. bug','aracnet'])
        if self.currentFloor >= 15:
            l.append('troll')
        if self.currentFloor >= 22:
            l = ["will o' wisp",]
        if self.currentFloor == 23 and self.parent.bDef['ogre'] == False:
            l = ('ogre',)
        if self.currentFloor >= 25:
            l = ['b. snake',]
        if self.currentFloor == 100 and self.parent.bDef['devil'] == False:
            l = ('devil',)
        return l

    def spawnMon(self): # Needs improvemet
        l = self.get_monList()
        shuffle(l)
        mon = genMon(monClass=l[0],lvl=self.currentFloor)
        return mon

    def explore(self):
        if randint(0,30)%2 == 0:
            sprint('Monster encountered.'); print()
            monster = self.spawnMon()
            self.parent.bSys.combatLoop(monster)
        elif randint(0,30)%3 == 0 and self.currentFloor == \
            self.parent.maxFloor and self.currentFloor < 100:
                flrBoss = {23:'ogre',35:'ghoul',100:'devil'}
                if self.currentFloor not in flrBoss.keys() or \
                    self.parent.bDef[flrBoss[self.currentFloor]] == True:
                        sprint('You found the stairs.'); print()
                        self.parent.maxFloor += 1
        else:
            sprint('Nothing happened.')


class Town(SubWorld):

    def com_seq(self):
        print()
        com = super().com_seq(state='town')
        if com == 'dungeon':
            sprint('You moved to the dungeon.')
            print()
            self.parent.dungeon.com_seq()
        elif com == 'save':
            self.parent.saveState()
        elif com == 'guild':
            sprint('You moved to the guild.')
            print()
            self.parent.guild.com_seq()
        elif com == 'store':
            sprint('Not available')
        elif com == 'status':
            self.parent.player.status()
        elif com == 'inventory':
            self.parent.player.items()
        elif com == 'equipment':
            self.parent.player.equipment()
            print()
            self.parent.msSys.equip()
        elif com == 'medic':
            if self.parent.player.inventory['gold'] >= 10:
                sprint('Healing will cost you 10 gold.')
                Confirm = confirm()
                if Confirm.lower() in ('y','yes'):
                    self.parent.player.rest()
                    self.parent.player.inventory['gold'] -= 10
                    self.parent.lDay += 1
                    sprint('Fatigue recovered.')
                else:
                    sprint('You did not get healed.')
            else:
                sprint('You don\'t have enough money')
            print()
        elif com == 'exit':
            self.parent.freePlay = False


class Guild(SubWorld):

    def com_seq(self):
        print()
        com = super().com_seq('guild')
        if com == 'calendar':
            day = self.parent.get_currentDay()
            sprint('This is day %d'%day)
        elif com == 'status':
            self.parent.player.status()
        elif com == 'inventory':
            self.parent.player.items()
        elif com == 'equipment':
            self.parent.player.equipment()
            print()
            self.parent.msSys.equip()
        elif com == 'return to town':
            sprint('You moved back to the town')
        elif com == 'sell':
            self.parent.msSys.sell()
        elif com == 'learn skills':
            sprint('You can learn the following skills:')
            self.parent.msSys.learnSkill()
        elif com == 'quests':
            self.parent.qSys.menu()
        if com != 'return to town':
            self.com_seq()


class UniWorldObj(World):

    def __init__(self,dPath):
        self.dPath = dPath
        try:
            self.player = loadChar(self.dPath)
            d = loadWorldVars(self.dPath)
        except FileNotFoundError:
            self.player = genChar()
            d = {'mFloor':1,'time':0, 'quest':{}, \
                    'bDef':{'devil':False,'ogre':False,'ghoul':False}}
        self.sTime = t()
        self.lDay = d['time']
        self.maxFloor = d['mFloor']
        self.town = Town(self)
        self.dungeon = Dungeon(self)
        self.guild = Guild(self)
        self.bSys = BattleSys(self)
        self.msSys = SelecSys(self)
        self.qSys = QuestSys(self,d['quest'])
        self.bDef = d['bDef']
        self.freePlay = True

    def resetClock(self):
        self.sTime = t()

    def freePlayLoop(self):
        while self.freePlay == True:
            self.town.com_seq()
        exitGame()

    def get_currentDay(self):
        return get_days(self.sTime,self.lDay)

    def saveState(self):
        self.player.dumpStats(self.dPath)
        dumpWorldVars(self.maxFloor,\
                get_days(self.sTime,self.lDay),self.bDef,self.dPath,self.qSys.get_state())
        sprint('Saved successfully.')


#______ Testing

if __name__ == '__main__':
    pass
