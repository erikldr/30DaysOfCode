n = int(input().strip())
n = str(bin(n)[2:]).split("0")

maior = 0
for x in n:
    if len(x) > maior:
        maior = len(x)

print(maior)





