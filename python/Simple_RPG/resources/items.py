# Item objects
#___________ Imports and related

#___________ Objects

class Item(object):
	
	""" Items """
	
	ITEMS = ('potion','d. slayer 3','d. slayer 2','d. slayer 1', \
	'f. elexir','knife','club','g. boots','gram','b. robe','gold')
	
	def __init__(self,itemStr,obj):
		self.name = itemStr
		d = obj.ITEMS
		if obj == equipItem:
			self.reqJob = (d[self.name])[3]
			self.eType = (d[self.name])[4]
		self.bonus = [(d[self.name])[0],(d[self.name])[1]]
		self.cost = (d[self.name])[2]
		
	def __str__(self):
		return self.name.title()
		
	def get_affStat(self):
		return self.bonus[0]
		
	def get_bonus(self):
		return self.bonus[1]
		
	def get_cost(self):
		return self.cost
		

class recItem(Item):
	
	ITEMS = {'potion':['hp',10,15],'f. elexir':['mp',10,15]}
	
	def __init__(self,itemStr):
		super().__init__(itemStr,recItem)
	
	
class equipItem(Item):
	
	ITEMS = {'d. slayer 3':['atk',75,0,'hero','weapon'], \
	'b. robe':['def',45,50000,'all','armor'], \
	'd. slayer 2':['atk',30,0,'all','weapon'],\
	'd. slayer 1':['atk',15,0,'all','weapon'],\
	'gram':['atk',60,65000,'all','weapon'],\
	'knife':['atk',5,20,'all','weapon'],\
	'club':['atk',7,35,'all','weapon'],\
	'g. boots':['agi',10,40,'ogre','foot']}
	
	def __init__(self,itemStr):
		super().__init__(itemStr,equipItem)
	
	def get_reqJob(self):
		return self.reqJob
		
	def get_eType(self):
		return self.eType

