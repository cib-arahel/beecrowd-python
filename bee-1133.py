#resto da dvisao

x = int(input())
y = int(input())

maior = 0
menor = 0

if x > y:
    maior = x
    menor = y
else:
    menor = x
    maior = y
    
if y > x:
    maior = y
    menor = x
else:
    menor = y
    maior = x
    
var = list(range(menor+1,maior))


for n in var:
    if n % 5 == 2 or n % 5 == 3:
        print(n)
