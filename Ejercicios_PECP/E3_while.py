"""
Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide -
 es plana. La pirámide se apila de acuerdo con un principio simple: cada capa 
 inferior contiene un bloque más que la capa superior.
"""
bloques = int(input("Ingrese cantidad de bloques: "))
bloques_usados = 0
cont = 1

while bloques_usados + cont <= bloques:
    print ("*" * cont)
    bloques_usados += cont
    if bloques_usados + cont <= bloques:
        cont += 1
print (f"La altura es de {cont} bloques.")

