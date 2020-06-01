

def start(spel):
    ja = ['ja', 'j', 'yes', 'zeker' , 'graag', 'leuk', 'oke', 'y']
    nee = ['nee', 'n', 'no', 'stop', 'quit']
    spelen = True
    while spelen == True:
        begin = input('Wil je {spel} spelen? '.format(spel = spel))
        if begin in ja:    
            return True
        elif begin in nee:
            return False
        else:
            print('Ik kan je reactie niet plaatsen')

winst_verlies_stand = {'gewonnen' : 0, 'verloren' : 0}

def w_v(winst, verlies):
    winst_verlies_stand['gewonnen'] += int(winst)
    winst_verlies_stand['verloren'] += int(verlies)
    print('je hebt nu {} keer gewonnen en {} keer verloren.'.format(winst_verlies_stand['gewonnen'], winst_verlies_stand['verloren'] ))

