
total = 0
lista1 = open("day1.txt", "r")
numeros = []

for elemento in lista1:
    for x in elemento:
        if(x.isnumeric()):
            numeros.append(int(x))
    valor = int(str(numeros[0]) + str(numeros[-1]))
    numeros.clear()
    total += valor

print(numeros)   
print(total)
