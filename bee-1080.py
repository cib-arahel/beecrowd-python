#maior e posição

maior = 0
imp = []

for i in range (1, 101):
    n = int(input())
    imp.append(n)

    for n in imp:
        if n > maior:
            maior = n


print(maior)
print(imp.index(maior)+1)
    
