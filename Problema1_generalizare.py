# Un sir de cararctere reprezinta numele si prenumele persoanei
# Stabiliti daca sirul dat este un nume corect de persoana
s=str(input('Introdu sirul de caractere: '))
a,b=s.split()
print(a)
print(b)
type(a)
type (b)
x=a.title()
y=b.title()
if ((x==a) and (y==b)):
    print('Sirul poate fi numele unei persoane')
else:
    print('Sirul nu poate fi nume de persoana')