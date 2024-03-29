# Creature and related objects: Player, NPC, Monster
#_____________ Imports, Variables, Functions

from random import randint
from skills import *
from items import *
from misc_functions import *
from math import fabs
from pickle import dump


#_____________ Objects

class Creature(object):
    """ World Residents(Super Class) """

    STATS = {"lvl":0,"hp":1,"mp":2,"atk":3,"def":4,"agi":5}
    JOBS = {'<none>':[0,0,0,0,0],'villager':[0,0,0,0,0],
            'knight':[5,0,0,0,0],'mage':[0,5,0,0,0],
            'paladin':[0,0,3,0,0],'sorcerer':[0,5,1,0,0],
            'hero':[10,10,5,5,5],'mage knight':[3,2,1,1,1]}

    def __init__(self, name = " ", skills = [], elem = '<none>'):
        self.job = 'creature'
        self.elem = elem
        self.name = name
        self.bstats = [1,0,0,0,0,0]   #(Lvl,HP,MP,Atk,Def,Agi)
        self.equipTemp = {'weapon':'none','armor':'none', 'foot':'none'}
        self.equips = self.equipTemp.copy()
        self.eBonusTemp = [0,0,0] #(Atk,Def,Agi)
        self.eBonus = self.eBonusTemp.copy()
        self.upBonus = (0,0,0,0,0) #(HP,MP,Atk,Def,Agi)
        self.HP = self.bstats[1]
        self.MP = self.bstats[2]
        self.skills = skills

    def __str__(self):
        return ("{0}-{1}: Level-{2}").format(self.job.title(),
                                             self.name.title(),
                                             self.bstats[0])

    def altStat(self,stat,val):
        self.bstats[Creature.STATS[stat]] = val

    def assignStats(self,sList):
        x = list(Creature.STATS.keys())
        for i in range(6):
            self.altStat(x[i],sList[i])
        self.HP = self.bstats[1]
        self.MP = self.bstats[2]

    def assignUpBonus(self,upList):
        self.upBonus = upList

    def equip(self,itemStr):
        x = Creature.STATS
        equip = equipItem(itemStr)
        if equip.get_reqJob() in ('all',self.job):
            self.equips[equip.get_eType()] = itemStr
            bkey = equip.get_affStat()
            self.eBonus[x[bkey]-3] = equip.get_bonus()

    def tDmg(self,target,spell=None,strike=None):
        tdef = target.bstats[4] + target.eBonus[1]
        satk = self.bstats[3] + self.eBonus[0]
        dmg:int = 0
        if (spell,strike) == (None,None):
            dmg = (satk - tdef)
        elif spell != None and strike == None:
            spell = Spell(spell)
            dmg = spell.get_dmg(target.elem)
        elif strike != None and spell == None:
            strike = Strike(strike)
            dmg = ((satk+satk*strike.get_dmgMult())-tdef)
        if dmg <= 0:
            dmg = 1
        return dmg

    def attack(self,target,spell=None,strike=None):
        dmg = self.tDmg(target,spell,strike)
        if spell != None:
            mpCost = Spell(spell).get_cost()
            self.MP -= mpCost
            sprint('%s used %s.'%(self.name.title(),spell.title()))
        if strike != None:
            mpCost = (Strike(strike).get_cost())*self.bstats[2]
            self.MP -= mpCost
            sprint('%s used %s.'%(self.name.title(),strike.title()))
        if spell == None:
            if randint(1,50)%10 == 0:
                lucky = self.agiToss(target,'luck')
                if lucky == 0:
                    dmg = 0
                    sprint('Attack missed.')
                elif lucky == 1:
                    dmg *= 2
                    sprint('Critical hit.')
        sprint('%s recieved %d damage.'%(target.name,dmg))
        target.HP -= dmg
        if target.HP < 0:
            target.HP = 0
            name = target.name
            sprint('%s has died.'%name.title())

    def status(self):
        print('_'*30); print()
        info = ('{0} - {1}'.format(self.job.title(), self.name.title()))
        sprint(info,'\t')
        print()
        sprint("Element: {}".format(self.elem.title()))
        x = list(Creature.STATS.keys())
        lvl = self.bstats[0]
        chp = self.HP; mhp = self.bstats[1]
        cmp = self.MP; mmp = self.bstats[2]
        sprint('Level : %d' % lvl)
        sprint('HP : %d / %d' % (chp,mhp))
        sprint('MP : %d / %d' % (cmp,mmp))
        for i in range(3,6,1):
            stat = x[i].title()
            val = self.bstats[i]
            bonus = self.eBonus[i-3]
            sprint("{0} : {1}(+{2})".format(stat,val,bonus))
        print(); print()
        sprint('Skills:')
        for i in self.skills:
            sprint(i.title())
        if len(self.skills) == 0:
            sprint('<None>')
        print('_'*30)

    def lvlUp(self):
        self.bstats[0] += 1
        for i in range(1,6):
            self.bstats[i] += self.upBonus[i-1]
        self.HP = self.bstats[1]
        self.MP = self.bstats[2]

    def goToLvl(self,lvl):
        lvlDiff = (lvl-self.bstats[0])
        if lvlDiff > 0:
            for i in range(lvlDiff):
                self.lvlUp()
        elif lvlDiff < 0:
            self.bstats[0] = lvl
            self.maxExp = 0

    def agiToss(self,target,boolType='first'):
        sagi = self.bstats[5]
        tagi = target.bstats[5]
        diff = int(fabs(sagi-tagi))
        if diff == 0:
            diff = 1
        if boolType == 'first':
            pFirst = True
            if sagi >= tagi:
                pFirst = True
            elif sagi < tagi:
                pFirst = False
            return pFirst
        elif boolType=='luck': # Needs improvement
            faster = self.agiToss(target=target)
            if faster == True:
                x = (randint(1,100) % 3 == 0)
            else:
                x = (randint(1,100) % 5 == 0)
            return 1 if (x == True or faster == True) else 0

class Player(Creature):

    def __init__(self, name = " "):
        super().__init__(name = name, elem = 'holy')
        self.job = "villager"
        self.jobBonus = [0,0,0,0,0] # Same as upBonus
        self.exp = 0
        self.maxExp = 100
        self.inventory = dict()

    def recover(self, item = None):
        self.inventory[item] -= 1
        item = recItem(item)
        affStat = item.get_affStat()
        bonus = item.get_bonus()
        if affStat == 'hp':
            self.HP += bonus
        elif affStat == 'mp':
            self.MP += bonus
        if self.HP > self.bstats[1]:
            self.HP = self.bstats[1]
        if self.MP > self.bstats[2]:
            self.MP = self.bstats[2]

    def altJob(self,job):
        if job in Creature.JOBS.keys():
            self.job = job
            for i in range(0,5,1):
                self.jobBonus[i] += (Creature.JOBS[job])[i]
            sprint("Job changed to '{}'.".format(job.title()))
        else:
            sprint('Invalid job.')

    def changeJob(self,lvl):
        newJob = 'none'
        if lvl == 10:
            sprint('Please select an new job:')
            sprint(' Knight(0): Increased HP bonus')
            sprint(' Mage(1): Increased MP bonus')
            jobDict10 = {}
            jobDict10[0] = 'knight'
            jobDict10[1] = 'mage'
            choice = promptCom(jobDict10)
            newJob = jobDict10[choice]
        elif lvl == 25:
            if self.job == 'knight':
                newJob = 'paladin'
            elif self.job == 'mage':
                newJob = 'sorcerer'
            self.addItem('d. slayer 1')
        if lvl== 40:
            newJob = 'mage knight'
            self.addItem('d. slayer 2')
        self.altJob(newJob)

    def addSkill(self,skill):
        if skill not in self.skills:
            if skill in Skill.SKILLS:
                self.skills.append(skill)
                sprint("Skill '{}' has been added.".format\
                        (skill.title()))
            else:
                sprint('Invalid skill.')
        else:
            sprint('Skill already learnt.')

    def altSkillSet(self,skillSet):
        self.skills = skillSet

    def addItem(self,itemStr, quantity = 1):
        if itemStr not in self.inventory.keys():
            self.inventory[itemStr] = 0
            for i in range(quantity):
                self.inventory[itemStr] += 1
        else:
            self.inventory[itemStr] += quantity

    def unEquip(self): #Prototype
        eSet = self.equips.values()
        for item in (x for x in eSet if x != 'none' ):
            self.addItem(item,1)
        self.equips = self.equipTemp.copy()
        self.eBonus = self.eBonusTemp.copy()

    def lvlUp(self):
        super().lvlUp()
        for i in range(1,6):
            self.bstats[i] += self.jobBonus[i-1]
        self.maxExp += (self.bstats[0])*10
        self.exp = 0
        sprint('Current level: %d'%self.bstats[0])

    def status(self):
        super().status()
        if self.bstats[0] < 100:
            print()
            sprint('Exp required for lvl up:  %s'\
                    %(self.maxExp-self.exp))
            print()
            print('_'*30)

    def equipment(self):
        d = self.equips
        k = tuple(self.equips.keys())
        print()
        sprint('Current equipments: ')
        for i in range(3):
            type = (k[i]).title()
            name = (d[type.lower()]).title()
            astat = (('atk','def','agi')[i]).title()
            bonus = self.eBonus[i]
            sprint('%s: %s (%s: +%d)'%(type,name,astat,bonus))

    def items(self):
        d = self.inventory
        print()
        if len(d) > 0:
            sprint('Following items are owned:')
            for i in d.keys():
                sprint('%s: %d'%(i.title(),d[i]))
        else:
            sprint('No items owned.')

    def removeItem(self,item):
        self.inventory[item] -= 1
        if self.inventory[item] <= 0:
            del self.inventory[item]

    def sell(self,itemStr):
        try:
            item = recItem(itemStr)
        except KeyError:
            item = equipItem(itemStr)
        self.addItem('gold',item.get_cost())
        self.removeItem(itemStr)

    def gainExp(self,exp=0):
        sprint('%d exp gained.'%exp)
        if self.bstats[0] < 100:
            self.exp += exp
            if self.exp >= self.maxExp:
                exp = self.exp-self.maxExp
                self.lvlUp()
                self.maxExp += (10*(self.bstats[0]))
                if self.bstats[0] in (10,25,40):
                    print()
                    self.changeJob(self.bstats[0])
                self.gainExp(exp)
        else:
            pass

    def reducedStatus(self):
        bhp = self.bstats[1]
        bmp = self.bstats[2]
        chp = self.HP; cmp = self.MP
        sprint(self)
        sprint('HP: %d/%d'%(chp,bhp))
        sprint('MP: %d/%d'%(cmp,bmp))

    def rest(self):
        self.HP = self.bstats[1]
        self.MP = self.bstats[2]

    def dumpStats(self,path):
        with open((path+'/playerDump.txt'),'wb') as file:
            toDump={'stats':self.bstats,'items':self.inventory,\
                    'equips':self.equips,'skills':self.skills,'job':self.job,\
                    'upBonus':self.upBonus,'eBonus':self.eBonus,\
                    'name':self.name,'exp':self.exp,'mExp':self.maxExp,\
                    'hp':self.HP,'mp':self.MP,'equips':self.equips,\
                    'jobBonus':self.jobBonus}
            dump(toDump,file)


class Monster(Creature):

    SET = {'slime':['null',[1,15,0,10,2,1],(5,0,1,1,1),(),()], \
            'devil':['dark',[1,30,20,15,5,5],(15,10,3,2,3),\
            ('hell fire',),('gram','b. robe')],\
            'goblin':['null',[1,20,0,12,3,4],(5,0,2,1,1),(),()],\
            'orc':['dark',[1,15,0,10,5,4],(5,0,2,2,1),(),('knife',)],\
            'sp. bug':['elec',[1,20,10,2,1,4],(5,3,1,1,3),('spark',),()],\
            'aracnet':['elec',[1,20,20,3,2,5],(5,5,1,1,4),('v. shot',),()],\
            'troll':['dark',[1,30,1,2,3,1],(5,1,2,3,1),(),('club',)],\
            "will o' wisp":['fire',[1,20,20,4,2,1],(5,5,2,2,2),('blaze',),()],\
            'ogre':['dark',[1,30,0,3,3,1],(10,0,4,3,1),(),('g. boots',)],\
            'b. snake':['water',[1,25,15,4,2,4],(10,10,2,2,3),('a. jet',),()]}
    # Needs a proper database

    def __init__(self, job='monster', skills=[],\
            elem = 'null'):
        super().__init__(job,skills,elem)
        self.job = job

    def __str__(self):
        return("%s: Level-%d"%(self.job.title(),self.bstats[0]))

    def terminate(self,player):
        for i in self.equips.values():
            if i != 'none':
                if randint(0,50)%4 == 0:
                    sprint("'%s' obtained."%i.title())
                    if i not in player.inventory.keys():
                        player.inventory[i] = 1
                    elif i in player.inventory.keys():
                        player.inventory[i] += 1
        baseExpOut = 10+(self.bstats[0])*5
        expOut = baseExpOut
        if self.bstats[0] > player.bstats[0]:
            lvlDiff = self.bstats[0]-player.bstats[0]
            expOut *= (lvlDiff+1)
        player.gainExp(expOut)

    def reducedStatus(self):
        chp = self.HP
        bhp = self.bstats[1]
        sprint(self)
        sprint('HP: %d/%d'%(chp,bhp))

#_____________
