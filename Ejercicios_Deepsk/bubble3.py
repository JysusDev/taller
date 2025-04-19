lista = [8, 5, 3, 2, 1]

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