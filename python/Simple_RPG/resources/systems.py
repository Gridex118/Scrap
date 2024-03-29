# System objects
# Battle system, Misc. selec. system

#________ Imports

from creature import *
from spec_functions import *
from items import *
from skills import *
from random import randint,shuffle

#________ Objects
class System(object):

    def __init__(self,parent):
        self.parent = parent


class BattleSys(System):

    dBosses = ('devil','ogre','ghoul')

    def comSelect(self,state):
        print()
        com = get_com(state)
        return com

    def combatLoop(self,mon): #Needs improvement
        p = self.parent
        playerTurn = p.player.agiToss(mon)
        if mon.name in BattleSys.dBosses:
            bState = 'b. battle'
        else:
            bState = 'n. battle'
        while True:
            print()
            p.player.reducedStatus()
            print()
            mon.reducedStatus()
            print()
            if p.player.HP <= 0 or mon.HP <= 0:
                if mon.HP <= 0:
                    mon.terminate(p.player)
                    if mon.job in BattleSys.dBosses:
                        p.bDef[mon.job] = True
                        p.player.gainExp(100*mon.bstats[0])
                        if mon.job == 'devil':
                            sprint('Game completed in %d days.'%(p.get_currentDay()))
                    break
                elif p.player.HP <= 0:
                    print()
                    sprint('You have died in battle. Game Over.')
                    exitGame()
            if playerTurn == True:
                com = self.comSelect(bState)
                if com == 'attack':
                    p.player.attack(mon)
                elif com == 'inventory':
                    p.player.items()
                elif com == 'status':
                    p.player.status()
                elif com == 'spells':
                    choice = self.spellAtk()
                    if choice == 'return':
                        continue
                    else:
                        if Spell(choice).get_cost() <= p.player.MP:
                            p.player.attack(mon,spell=choice)
                        else:
                            sprint('You do not have enough MP')
                            continue
                elif com == 'strike skills':
                    choice = self.strikeAtk()
                    if choice == 'return':
                        continue
                    else:
                        if Strike(choice).get_cost() * p.player.bstats[2] <= p.player.MP:
                            p.player.attack(mon,strike=choice)
                        else:
                            sprint('You do not have enough MP')
                            continue
                elif com == 'recover':
                    continue
                elif com == 'run':
                    if randint(0,30)%2 == 0:
                        sprint('...You ran away.')
                        break
                    else:
                        sprint('Could not run away.')
                if com in ('attack','spells','strike skill','recover',\
                        'run'):
                    playerTurn = False
                else:
                    continue
            elif playerTurn == False:	
                self.monAtk(mon,p.player)
                playerTurn = True

    def spellAtk(self):
        allSOwn = [x for x in self.parent.player.skills]
        Spells = [x for x in allSOwn if x in Spell.SKILLS.keys()]
        count = 0
        sDict = {}
        for spell in Spells:
            sDict[count] = spell
            sInfo = (spell,count,Spell(spell).get_cost())
            sprint('%s (%d) -%d MP'%sInfo)
            count += 1
        sDict[count] = 'return'
        sprint('return (%d)'%count)
        choice = sDict[promptCom(sDict)]
        return choice

    def strikeAtk(self):
        allSOwn = [x for x in self.parent.player.skills]
        Strikes = [x for x in allSOwn if x in Strike.SKILLS.keys()]
        count = 0
        sDict = {}
        for strike in Strikes:
            sDict[count] = strike
            bstats = self.parent.player.bstats
            bmp = bstats[2]
            sInfo = (strike,count,Strike(strike).get_cost()*bmp)
            sprint('%s (%d) -%d MP'%sInfo)
            count += 1
        sDict[count] = 'return'
        sprint('return (%d)'%count)
        choice = sDict[promptCom(sDict)]
        return choice

    def monAtk(self,mon,player): #Dmg comparison needed
        spells = [x for x in mon.skills if x in Spell.SKILLS.keys()]
        strikes = [x for x in mon.skills if x in Strike.SKILLS.keys()]
        atkDmg = {}
        atkDmg['basic'] = mon.tDmg(player)
        for strike in strikes:
            atkDmg[strike] = mon.tDmg(player,strike=strike)
        for spell in spells:
            atkDmg[spell] = mon.tDmg(player,spell=spell)
            if mon.tDmg(player,spell=spell) > \
                    mon.tDmg(player)\
                    and mon.MP >= Spell(spell).get_cost():
                mon.attack(player,spell=spell)
                break
        else:
            mon.attack(player)

class SelecSys(System):

    def equip(self):
        p = self.parent
        inv = p.player.inventory
        allEquips = equipItem.ITEMS.keys()
        currEquips = p.player.equips.values()
        toDisp = [x for x in allEquips if x not in currEquips]
        ownedEquips = [x for x in inv if x in toDisp if \
                (p.player.job == equipItem(x).get_reqJob()) or \
                equipItem(x).get_reqJob() == 'all']
        count = 0; eDict = {}
        for item in ownedEquips:
            eDict[count] = item
            count += 1
        eDict[count] = 'unequip all items'
        eDict[count+1] = 'return'
        self.equipOpts(eDict)

    def equipOpts(self,eDict):
        p = self.parent
        sprint('Available options:'); print()
        for ind in eDict.keys():
            if eDict[ind] not in ('return','unequip all items'):
                x = equipItem(eDict[ind])
                fTuple = (eDict[ind].title(),x.get_affStat(),\
                        x.get_bonus(),ind)
                sprint('Equip %s (%s +%d) (%d)'%fTuple)
            elif eDict[ind] in ('return','unequip all items'):
                sprint('%s (%d)'%(eDict[ind],ind))
        print()
        choice = promptCom(eDict)
        notToRemove = []	
        if eDict[choice] not in  ('return','unequip all items'):
            for i in p.player.equips.items():
                if i[1] != 'none':
                    if i[0] != equipItem(eDict[choice]).get_eType():
                        notToRemove.append(i)
            p.player.unEquip()
            for i in notToRemove:
                p.player.equip(i[1])
                p.player.removeItem(i[1])
            p.player.equip(eDict[choice])
            p.player.removeItem(eDict[choice])
            sprint('Item equipped.')
        elif eDict[choice] == 'unequip all items':
            p.player.unEquip()
            sprint('Items unequipped.')
        elif eDict[choice] == 'return':
            sprint('....')

    def sell(self):
        p = self.parent
        items = [i for i in p.player.inventory.keys() if i != 'gold']
        d = {}; index = 0
        for i in items:
            if i in equipItem.ITEMS.keys():
                cost = equipItem(i).get_cost()
            elif i in recItem.ITEMS.keys():
                cost = recItem(i).get_cost()
            tup = (i.title(),p.player.inventory[i],cost,index)
            sprint('%s (X %d) - %d gold (%d)'%tup)
            d[index] = i
            index += 1
        sprint('Return (%d)'%index)
        d[index] = 'return'
        com = d[promptCom(d)]
        if com == 'return':
            sprint('....')
        else:
            if confirm(" Sell '%s' (y/n):   "%com).lower() == 'y':
                p.player.removeItem(com)
                if i in equipItem.ITEMS.keys():
                    cost = equipItem(i).get_cost()
                elif i in recItem.ITEMS.keys():
                    cost = recItem(i).get_cost()
                p.player.inventory['gold'] += cost
                sprint('You earned %d gold.'%cost)
            else:
                print('......')
        print()

    def learnSkill(self):
        p = self.parent
        allSpls = [s for s in Spell.SKILLS]
        allStr = [s for s in Strike.SKILLS]
        avSpls = [s for s in allSpls if Spell(s).get_reqLvl() <= p.player.bstats[0] and s not in p.player.skills]
        avStr = [s for s in allStr if Strike(s).get_reqLvl() <= p.player.bstats[0] and s not in p.player.skills]
        avSkills = []
        for i in (avSpls,avStr):
            avSkills.extend(i)
        d = {}; ind = 0; costs = {}
        for s in avSkills:
            if s in Spell.SKILLS.keys():
                dmg = Spell(s).get_dmg()
                cost = (10+Spell(s).get_reqLvl()*10)
            elif s in Strike.SKILLS.keys():
                dmg = p.player.bstats[3] + \
                        (Strike(s).get_dmgMult()*p.player.bstats[3])
                cost = (5+Strike(s).get_reqLvl()*5)
            costs[s] = cost
            tup = (s.title(),dmg,cost,ind)
            sprint('%s-%d DMG-%d Gold (%d)'%tup)
            d[ind] = s
            ind += 1
        sprint('Return (%d)'%ind)
        d[ind] = 'return'
        print()
        com = d[promptCom(d)]
        if com == 'return':
            print('.....')
        else:
            if p.player.inventory['gold'] >= costs[com]:
                p.player.addSkill(com)
                p.player.inventory['gold'] -= costs[com]
            else:
                sprint('You do not have enough money.')
        print()

    def selQuest(self):
        currQuest = self.parent.qSys.cQuest
        if currQuest in ('none',None):
            quests = self.parent.qSys.QUESTS
            if len(quests) > 0:
                d = {}; count=0
                for i in quests.keys():
                    d[count] = quests[i]
                    tup = ((quests[i])[2],(quests[i])[0],(quests[i])[1],i)
                    sprint('%s %s. {%s} (%d)'%tup)
                    count += 1
                d[count] = 'return'
                sprint('Return (%d)'%count)
                print()
                comInd = promptCom(d)
                com = d[comInd]
                if com == 'return':
                    print('.......')
                else:
                    sprint("Quest '%s' accepted." % com[0])
                    self.parent.qSys.set_quest(com)
                    del quests[comInd]
            else:
                sprint('No quests available.')
        else:
            sprint('Please complete your current quest first.')


class QuestSys(System):

    QUESTS = {0:['knife','100 exp','fetch']}

    def __init__(self,parent,quests):
        super().__init__(parent)
        try: 
            self.load_state(quests)
        except KeyError:
            self.cQuest = None
            self.reward = None

    def addQuest(self,questL):
        QuestSys.QUESTS[len(QuestSys.QUESTS)] = questL

    def menu(self):
        sprint('Current quest: %s'%(self.cQuest))
        print()
        d = {} ; count = 0
        for i in ('available quests','submit','return'):
            sprint('%s (%d)'%(i.title(),count))
            d[count] = i
            count += 1
        print()
        com = d[promptCom(d)]
        if com == 'return':
            print('.....')
        elif com == 'available quests':
            print()
            self.parent.msSys.selQuest()
        elif com == 'submit':
            if self.cQuest == None:
                print()
                sprint('You have not accepted any quests yet.')
            else:
                self.get_reward()

    def load_state(self,quest):
        self.cQuest = quest['cQuest']
        self.reward = quest['reward']
        QuestSys.QUESTS = quest['quests']

    def get_reward(self):
        questL = self.cQuest.split()
        rewardL = self.reward.split()
        if questL[0] == 'fetch':
            exp = int(rewardL[0])
            if questL[1] in self.parent.player.inventory.keys():
                sprint('Quest completed.')
                self.parent.player.removeItem(questL[1])
                self.parent.player.gainExp(exp)
                self.cQuest = None
                self.reward = None
            else:
                sprint('Quest still incomplete.')
        elif questL[0] == 'subjugation':
            ...
        else:
            print('....')

    def get_state(self):
        return {'quests':QuestSys.QUESTS,'reward':self.reward,'cQuest':self.cQuest}

    def set_quest(self,quest):
        self.cQuest = ('%s %s'%(quest[2],quest[0]))
        self.reward = quest[1]
