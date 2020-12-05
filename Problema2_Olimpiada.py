# Trei purcei au impartit frateste n alune, cele ramase le-au dat Ritei. Realizti un program care, cititnd de la tastatura nr de alune
# Sa ne afiseze la ecran cate alune au revenit fiecarui purcel si cate alune au ramas pentru Rita
n=int(input('Introdu nr de alune: '))
if n%3==0:
    y=n/3
    print('Fiecare purcel are ', y ,' alune')
else:
    y=n//3
    z=n-3*y
    print('Fiecare purcel are', y, 'alune')
    print('Rita are', z, 'alune' )