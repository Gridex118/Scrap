# Miscellaneous Functions
#________


def sprint(string, spacing = " ", end = "\n"):
	print("{0}{1}".format(spacing, string), end = end)
	
def confirm(str=' Continue (y/n):   '):
	_conf_ = input(str)
	if _conf_.lower() not in ('n','no','y','yes'):
		_conf_ = confirm()
	elif _conf_ in ('y','yes'):
		_conf_ == 'y'
	elif _conf_ in ('n','no'):
		_conf_ = 'n'
	return _conf_

def promptCom(dictionary={}):
	d = dictionary
	l = list(d.items())
	try:
		command = int(input(' Select a command: '))
		if command not in (x[0] for x in l):
			raise ValueError
	except ValueError:
		command = promptCom(dictionary=d)
	return command