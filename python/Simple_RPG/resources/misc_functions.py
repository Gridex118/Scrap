# Miscellaneous Functions
#________


def sprint(string, spacing = " ", end = "\n"):
    print("{0}{1}".format(spacing, string), end = end)

def confirm(prompt=' Continue (y/n):   '):
    _conf_ = input(prompt)
    if _conf_.lower() not in ('n','no','y','yes'):
        return confirm()
    elif _conf_ in ('y','yes'):
        return 'y'
    elif _conf_ in ('n','no'):
        return 'n'

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
