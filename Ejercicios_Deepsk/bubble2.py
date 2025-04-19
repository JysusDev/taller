lista = [5, 3, 8, 1, 2]

swaped = True
cont = 0

while swaped:
    swaped = False
    for i in range(len(lista) -1):
        if lista[i] < lista[i + 1]:
            swaped = True
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
    cont += 1
print(lista)
print(cont)
