#intervalo 2

N = int(input())

i = 1
somain = 0
somaout = 0

while i <= N :
    x = int(input())
    
    
    if x >= 10 and x <= 20:
        somain = somain + 1
    else:
        somaout = somaout + 1

    i += 1
    
print(f"{somain} in")
print(f"{somaout} out")
