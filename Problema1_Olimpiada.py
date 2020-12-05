# La o ferma avicola sunt x pasari. Jumatate din acestea sunt gaini. Nr de rate constituie un sfert din nr gainilor. Celelalte sun gaste.
#Scrieti un program care citeste de la tastatura nr total de pasari si afiseaza nr de gaini si rate.        
x=int(input('Introdu nr total de pasari: '))
print(x, 'pasari')
if x%2==0:
    y=x/2
    print(y, 'gaini')
else:
    y=int(x/2)
if y%4==0:
    z=y/4
    print(z, 'rate')
else:
    z=int(y/4)
g=x-y-z
print(g, 'gaste')