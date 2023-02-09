# 20 March, 2021
# A simple turn based rpg
# Ver 0.4.0(Fourth Beta)
# 黒白
# Project <M-002>

#___________Imports and variables

import sys,os
from random import seed
from time import time as t

seed = t()

def get_path(error=False):
	try:
		with open('resPath.txt','r') as file:
			PATH = str(file.read())
		if error:
			raise FileNotFoundError
	except FileNotFoundError:
		print(' Resource files not found.')
		print(' Related paths:')
		for i in sys.path:
			print('',i)
		print()
		PATH = input(' Please enter resource path:\n  ')
		print()
		with open('resPath.txt','w') as file:
			file.write(PATH)
	sys.path.append(PATH)

try:
	sys.path.append(os.getcwd()+'/resources')
	from world import *
except ModuleNotFoundError:
	try:
		get_path()
	except ModuleNotFoundError:
		get_path(error=True)
		print(' Path changed, please restart.')
		input(' Press ENTER to exit_')
		sys.exit()
		
#___________

def main():
	print('\t\tSimple RPG')
	print('\t\tVer 0.4.0(Fourth Beta Test)')
	print('_'*50)
	print()
	uni = UniWorldObj(os.getcwd()+'/dumps')
	uni.freePlayLoop()

#___________Main

if __name__ == '__main__':
	main()