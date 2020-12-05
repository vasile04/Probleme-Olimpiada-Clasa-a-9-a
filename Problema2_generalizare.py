import math
n=int(input('Introdu nr: '))
if len(str(n))<=70:
    r=math.sqrt(n)
    p=int(r)
    print(p)
    print(n-(p**2))
else:
    print ('Eroare')
