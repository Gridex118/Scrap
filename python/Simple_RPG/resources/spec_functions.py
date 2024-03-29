#Specialized Functions

#___________ Imports and Variables

from creature import *
from misc_functions import *
from random import randint
from sys import exit
from time import time as t
from math import ceil
from pickle import dump,load


#___________ Functions	

def getCharName():
    name = input(' Enter player name:  ')
    conf = input(" Continue with '%s': "%name.title())
    if conf.lower() in ('n','no'):
        name = getCharName()
    elif conf.lower() in ('y','yes'):
        name = name
    else:
        sprint('An error occured.')
        name = getCharName()
    return name

def genChar():
    sprint('Starting new game'); print()
    name = getCharName()
    print()
    lvl = 1
    bhp = randint(45,50); uhp = randint(15,18)
    bmp = randint(25,30); ump = randint(10,13)
    batk = randint(12,14); uatk = randint(2,3)
    bdef = randint(5,7); udef = randint(1,2)
    bagi = randint(6,8); uagi = randint(2,3)
    player = Player(name)
    player.assignStats([lvl,bhp,bmp,batk,bdef,bagi])
    player.assignUpBonus((uhp,ump,uatk,udef,uagi))
    player.addItem('gold',100)
    return player

def loadChar(path):
    try:
        with open((path+'/playerDump.txt'),'rb') as file:
            playerDict = load(file)
        sprint('Save file found.')
        name = playerDict['name']
        player = Player(name)
        player.job = playerDict['job']
        player.bstats = playerDict['stats']
        player.HP = playerDict['hp']
        player.MP = playerDict['mp']
        player.upBonus = playerDict['upBonus']
        player.jobBonus = playerDict['jobBonus']
        player.eBonus = playerDict['eBonus']
        player.inventory = playerDict['items']
        player.skills = playerDict['skills']
        player.exp = playerDict['exp']
        player.maxExp = playerDict['mExp']
        player.equips = playerDict['equips']
        sprint('Load complete.'); print()
        return player
    except KeyError:
        sprint('Error, save file is corrupted.')
        raise FileNotFoundError

def genMon(monClass,lvl):
    elem = (Monster.SET[monClass])[0]
    bskills = (Monster.SET[monClass])[1]
    upBonus = (Monster.SET[monClass])[2]
    skills = (Monster.SET[monClass])[3]
    equips = (Monster.SET[monClass])[4]
    monster = Monster(monClass,skills,elem)
    for equipment in equips:
        monster.equip(equipment)
    monster.assignStats(bskills)
    monster.assignUpBonus(upBonus)
    monster.goToLvl(lvl)
    return monster

def validCom(command,state='dungeon'):
    bool = True
    alwaysTrue = ('status','inventory')
    validCom = ()
    if state == 'dungeon':
        validCom = ('explore','return to town',\
                'equipment','save','go to next floor')
    elif state == 'town':
        validCom = ('medic','guild','save','dungeon',\
                'exit','equipment')
    elif state == 'n. battle':
        validCom = ('spells','attack','strike skills','run',\
                'recover')
    elif state == 'b. battle':
        validCom = ('spells','attack','strike skills',\
                'recover')
    elif state == 'guild':
        validCom = ('equipment','sell','buy','learn skills',\
                'quests','return to town','calendar')
    if command in validCom:
        bool = True
    elif command in alwaysTrue and state != 'selection':
        bool = True
    else:
        bool = False		
    return bool

def dispCommands(getDict = False,state='dungeon'):
    COMMANDS = ('status','inventory','equipment','save',\
            'explore','return to town','medic','dungeon','guild',\
            'attack','spells','strike skills','recover','run',\
            'go to next floor','calendar','exit','return','sell','buy',\
            'learn skills','quests')
    index = 0; d = {}
    for command in COMMANDS:
        if validCom(command,state):
            if not getDict:
                sprint('%s (%d)'%(command.title(),index))
            if getDict:
                d[index] = command
            index += 1
    if getDict:
        return d

def get_com(state='dungeon',invalid = False):
    d = dispCommands(state=state,getDict=True)
    if not invalid:
        sprint('Following commands are available: ')
        print()
        dispCommands(state=state); print()
    index = promptCom(dictionary=d)
    print()
    command = d[index]
    return command

def get_days(sTime,lDay=0):
    cTime = t()
    tElapsed = cTime - sTime
    days = ceil(tElapsed*(0.025))
    return (lDay+days)

def exitGame():
    input(' Press enter to exit_')
    exit()

def dumpWorldVars(floor,day,bDef,path,quest):
    with open((path+'/worldDump.txt'),'wb') as file:
        dump({'mFloor':floor,'time':day,'bDef':bDef,\
                'quest':quest},file)

def loadWorldVars(path):
    with open(path+'/worldDump.txt','rb') as file:
        return load(file)

#___________
