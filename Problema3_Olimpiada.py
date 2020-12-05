# sa se scrie un program care citeste un nr de ani si calculeaza nr de luni, zile si ore corespunzatoare.
# se considera ca un an are 365 zile
a=int(input('Introdu nr de ani: '))
n=a*12
print(n, 'luni')
z=a*365
print(z, 'zile')
o=z*24
print(o, 'ore')