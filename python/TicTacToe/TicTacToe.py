# Tic-Tac-Toe
# Started: 5 September, 2020
# Ver 5.0.1(Final +) 
# 黒白
# Project <M-001>

#____________


from random import randrange,seed,shuffle
from time import time
from probMap import probMap,sync
from pickle import dump,load

#____________


l = [1,2,3,4,5,6,7,8,9]
na = [0]
wl = [(l[0],l[1],l[2]),(l[3],l[4],l[5]),(l[6],l[7],l[8]),(l[0],l[3],l[6]), (l[1],l[4],l[7]),(l[2],l[5],l[8]),(l[0],l[4],l[8]),(l[2],l[4],l[6])]
RUN = True
GAME = True
#__________________

def boardm(mode = 'normal'):						  
	"""Makes game board."""
	if mode == 'normal':
		board = """ \t\t   {0}|{1}|{2} 
	         ___|_|___
	           {3}|{4}|{5}
    	         ___|_|___
	           {6}|{7}|{8} """.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])
		return board


def win(piece): 			# Check for winner
	global wl
	wl = [(l[0],l[1],l[2]),(l[3],l[4],l[5]),(l[6],l[7],l[8]),(l[0],l[3],l[6]), (l[1],l[4],l[7]),(l[2],l[5],l[8]),(l[0],l[4],l[8]),(l[2],l[4],l[6])]
	winln = (piece,piece,piece)
	win = False
	if wl[0] == winln or wl[1] == winln:
		win = True
	elif wl[2] == winln or wl[3] == winln:
		win = True
	elif wl[4] == winln or wl[5] == winln:
		win = True
	elif wl[6] == winln or wl[7] == winln:
		win = True		
	return win


def up_board(block,piece,mode = 'normal'):  
	"""Update board."""
	if mode == 'normal':
		global l
		l[block - 1] = piece
		na.append(block)
		Board = boardm()
		return Board


def first():
	"""Decide who goes first."""
	seed = time()
	seed = randrange((int(time())-100),int(time()))
	x = randrange(2)
	if x == 0:
		player = True
		print('You can go First.')
	elif x == 1:
		player = False
		print('I shall go First.')
	return player


def notNone(v,w,x=None,y=None,z=None):
	"""Returns first non-null value"""
	lst = [v,w,x,y,z]											 
	value = None											  
	for i in lst:
		value = i
		if value != None:
			return int(value)
			break
			

def sortDict(dictionary):
	"""Sorts dictionary based on values.""" 
	keys = list(dictionary.keys())						
	values = list(dictionary.values())
	values.sort( reverse = True )
	sortedDictionary = {}
	for i in values:
		for j in keys:
			if dictionary[int(j)] == int(i):
				sortedDictionary[int(j)] = int(i)
				keys.remove(j)
				break
	return sortedDictionary		

#______________________


class computer(object):
	
	def __init__(self):
		global player
		player = first()			
		
	def think(self):
		""" Main pseudo AI """
		block = 0
		workable = False
		keys = list(map.keys())
		if turn == 1:
			workable = True
			use = 0
			for i in (1,3,7,9):
				use = randrange(2)
				if use == 1:
					block = i
					break
			if block == 0:
				blockLast = [1,3,7,9]
				shuffle(blockLast)
				block = blockLast[0]
		elif int(map[keys[0]]) > 0:
			block = int(keys[0])
			workable = True
		if workable == False:
			while block in na:
				block = randrange(1,10)
		return block
		
	def look(self,lst,a,b,c,p1,p2,obj='bool'):
		"""Analyzes the board."""
		tb = None
		boolVar = (lst[a] == p1 and lst[b] == p1 and lst[c] != p2)
		if boolVar == True:
			tb = int(lst[c])
		if obj == 'bool':
			return boolVar
		elif obj == 'block':
			return tb
			
	def reflex(self,obj = 'mode'):
		""" Auxilary pseudo AI """
		mode = 'think'
		to_block = None
		for i in wl:           # Take the third blovk of an 'o' pair
			xxz,a = self.look(i,0,1,2,'o','x'),self.look(i,0,1,2,'o','x','block')
			zxx,b = self.look(i,1,2,0,'o','x'),self.look(i,1,2,0,'o','x','block')
			xzx,c = self.look(i,0,2,1,'o','x'),self.look(i,0,2,1,'o','x','block')
			lkb = notNone(a,b,c)
			if xxz or zxx or xzx:
				mode = 'victor'
				try:
					to_block = lkb
				except:
					mode = 'think'
				break
		if mode != 'victor':			
			for i in wl:             # Block Player's win
				xxz,a = self.look(i,0,1,2,'x','o'),self.look(i,0,1,2,'x','o','block')
				zxx,b = self.look(i,1,2,0,'x','o'),self.look(i,1,2,0,'x','o','block')
				xzx,c = self.look(i,0,2,1,'x','o'),self.look(i,0,2,1,'x','o','block')
				lkb = notNone(a,b,c)
				if xxz or zxx or xzx:
					mode = 'blocker'
					try:
						to_block = lkb
					except:
						mode = 'think'
					break		
		if obj == 'mode':
			return mode
		elif obj == 'bl':
			return to_block

	def com_play(self):
		"""Computer's Move"""
		block = 0		
		mode = self.reflex('mode')
		if mode == 'blocker' or mode == 'victor':
			block = self.reflex('bl')
		elif mode == 'think':
			block = self.think()
		return block
#_________________


print('\n\t\t\tTic-Tac-Toe\n')		# Main menu
print('\t  1. Play \t  2. Quit')  		
play = None
while play not in ('1','2'):
	play = input('\n\t(1/2)>> ')
if play == '2':
	RUN = False
print()
#________________						


def game():
	"""Game Play."""
	global board
	global player
	if player:
		pblock = 0
		while pblock in na or pblock > 9:
			try:
				pblock = int(input('Select a block :  '))
			except:
				pblock = 0
		board = up_board(pblock,'x')
	if not player:
		cblock = com.com_play()
		print('I choose block',cblock)
		board = up_board(cblock,'o')
	player = not player
		
def main():
	"""Preliminary Game Setup"""
	global l,com,turn,round,board,map
	if len(na) == 1:
		l = [1,2,3,4,5,6,7,8,9] ; board = boardm()
		com = computer()
		turn,round = 0,0
	win('x') 
	map = sortDict(probMap(na,wl))
	print(board) ; print()
	turn += 1 ; round = (turn/2)
	game()
#______________	


while RUN:
	while GAME:
		sync()
		try:
			with open('lossPatterns.txt','rb') as file:
				lossPatterns = load(file)
		except:
			lossPatterns = []
		main()
		if win('x') or win('o') or (len(na) == 10):
			print(board)
			if win('x'):
				print('You win....')
				if wl not in lossPatterns:
					lossPatterns.append(wl)
				with open('lossPatterns.txt','wb') as file:
					dump(lossPatterns,file)
			elif win('o'):
				print("It's my win.")
			else:
				print("It's a draw.")
			print()
			GAME = False
			RUN = 'standby'
			while RUN == 'standby':
				RUN = input(' Play Again(y/n):  ')
				if RUN.lower() not in ('y','n'):
					RUN = 'standby'
			if RUN.lower() == 'y':
				na = [0]
				RUN = True
				GAME = True
			else :
				RUN = False
		print()
#______________


print()
input('Press enter to exit.')		