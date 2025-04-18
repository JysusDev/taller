"""
Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide -
 es plana. La pirámide se apila de acuerdo con un principio simple: cada capa 
 inferior contiene un bloque más que la capa superior.
"""
bloques = int(input("Ingrese cantidad de bloques: "))
acum = bloques
cont = 0

while acum + cont <= bloques:
    cont += 1
    acum = acum - cont
print (cont)