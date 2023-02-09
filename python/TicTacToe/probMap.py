# probMap function
""" Maps the apparent 'worth' of a block """

#__________

from pickle import dump,load

#__________

def sync():
	global lossPatterns
	try:
		with open('lossPatterns.txt','rb') as file:
			lossPatterns = tuple(load(file))
	except FileNotFoundError:
		lossPatterns = tuple()

sync()

def invBlocks(wl,currentRow):
	
	invBlocks = []
	patRoster = {}
	
	for pattern in lossPatterns:
		mf = 0
		for i in range(len(wl)):
			if wl[i] == pattern[i]:
				mf += 1
		pattern_index = lossPatterns.index(pattern)
		patRoster[pattern_index] = mf
		
	for patInd in patRoster.keys():
		if (max(patRoster.values()) >= 1) and patRoster[patInd] == max(patRoster.values()):
			try:
				accPat = (lossPatterns[patInd])
				misMatch = 0
				index = wl.index(currentRow)
				accPat_row = accPat[index]
				if currentRow == accPat_row:
					pass
				else:
					for i in range(3):
						if currentRow[i] == accPat_row[i]:
							pass
						else:
							misMatch += 1
				if misMatch >= 2:
					pass
				elif misMatch == 1:
					for i in currentRow:
						if i not in accPat_row:
							invBlocks.append(i)
			except IndexError:
				pass
		
	return invBlocks
					

#__________

def probMap(na,wl):
	
	blocks = [1,2,3,4,5,6,7,8,9]
	for i in na:
		if i in blocks:
			blocks.remove(i)
	boardMap = {}
	for x in blocks:
		sf = 0; countX = 0
		for row in wl:
			if x in row:
				sf += 1; countX += 1
				if x in invBlocks(wl,row):
					sf = -(float('inf'))
				if 'o' in row:
					add = True
					for i in blocks:
						if i != x and i in row:
							if i in [1,3,7,9]:
								add = False ; break
					if add:
						sf += 1
				if 'x' in row:
					sf += (row.count('x')+1)
				for y in row:
					if y in blocks and y != x:
						countY = 0
						for rowOth in wl:
							if y in rowOth and x not in rowOth :
								if 'x' not in rowOth:
									if rowOth != row:
										countY += 1
				try:
					if countY > countX:
						sf -= 1
				except:
					pass			
		if sf < 0:
			sf = -1		
		boardMap[x] = sf
	return boardMap