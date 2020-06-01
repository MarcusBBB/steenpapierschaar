import st_start
import random

spelen = st_start.start('steen, papier, schaar')
keuzes = ['sc', 'st', 'pa']
keuzes_dict = {'st':'steen', 'pa':'papier', 'sc': 'schaar'}
while spelen == True:
    keuze = input('kies je steen (st), papier (pa) of schaar (sc)? om te stoppen kies q ' )
    if keuze == 'q':
        spelen = False
        break
    while keuze not in keuzes:
        keuze = input('Ik heb je keuze niet begrepen. Kies je steen (st), papier (pa) of schaar (sc)?')
    pc_keuze = random.choice(keuzes)
    print(pc_keuze)
    print('jij koos: {keuze} en de computer koos: {pc_keuze}'.format(keuze = keuzes_dict[keuze], pc_keuze = keuzes_dict[pc_keuze]))
    if keuze == pc_keuze:
        print('gelijk spel. Nog een keer?')
    elif keuze == 'st' and pc_keuze == 'sc' or keuze == 'sc' and pc_keuze == 'pa' or keuze == 'pa' and pc_keuze == 'st':
        print('gefeliciteerd! je hebt gewonnen.')
        st_start.w_v(1,0)
    else:
        print('Helaas, verloren.')
        st_start.w_v(0,1)
        
        
    #spelen = st_start.start('steen, papier, schaar')



print('Bedankt voor het spelen.')