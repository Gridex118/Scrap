# Skill objects
#____________ Imports and Related

def multiplier(sElem,tElem):
	advantage = None
	ADV = Skill.T_ADV
	for i in ADV:
		if (sElem,tElem) == i:
			advantage = True
			break
		elif (tElem,sElem) == i:
			advantage = False
			break
	return advantage

#____________ Objects

class Skill(object):

	T_ADV = [('fire','grass'),('grass','water'),('water','fire'), \
	('null','<none>'),('elec','water'),('<none>','null')]
	SKILLS = ('fire ball','spark','b. shot','a. jet',\
	'r. fist','b. edge','hell fire','v. shot','blaze','s. thrust')
	
	def __init__(self,skillStr,obj):
		self.name = skillStr
		if obj == Spell:
			self.elem = (obj.SKILLS[skillStr])[0]
		if obj == Spell: 
			x,y = 1,2
		else:
			x,y = 0,1
		self.pow = (obj.SKILLS[skillStr])[x]
		self.cost = (obj.SKILLS[skillStr])[y]
		self.reqLvl = (obj.SKILLS[skillStr])[-1]
		
	def __str__(self):
		return (self.name.title())
			
	def get_cost(self):
		return (self.cost/100)
		
	def get_reqLvl(self):
		return self.reqLvl


class Spell(Skill):
		
	""" Magic attack skills """
		
	SKILLS = {'fire ball':['fire',15,10,1], 'spark':['elec',15,10,1],\
	'b. shot':['dark',35,15,2],'hell fire':['dark',350,500,70],\
	'v. shot':['elec',40,25,10],'blaze':['fire',40,25,10],\
	'a. jet':['water',35,20,10]}
	
	def __init__(self,skillStr):
		super().__init__(skillStr,Spell)
	
	def get_dmg(self,tElem = 'null'):
		power = self.pow
		dmg = power
		if multiplier(self.elem,tElem) == False:
			dmg = power//2
		elif multiplier(self.elem,tElem) == True:
			dmg = power*2
		return dmg
		
	def get_cost(self):
		return self.cost
		
			
class Strike(Skill):
		
		""" Physical attack skills """
		
		SKILLS = {'r. fist':[15,10,1],'b. edge':[40,20,10],\
		's. thrust':[55,25,25]}
		
		def __init__(self,skillStr):
			super().__init__(skillStr,Strike)
		
		def get_dmgMult(self):
			return (self.pow/100)
		
#_____________ 

if __name__ == '__main__':
	print(Skill.T_ADV)
	print()
	fireBall = Spell('fire ball')
	redFist = Strike('red fist')
	print(fireBall.get_dmg('grass'))
	print(redFist)