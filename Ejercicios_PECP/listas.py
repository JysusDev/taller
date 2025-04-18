list = [1,2,3,4,5]
print(list)
#El valor posicional de la lista empieza en el 0

#Cambio de una posicion especifica de la lista
list[0] = 5
print(list)

#Nos dice la cantidad de posiciones que tiene la lista
print(len(list))

#Comando de eleminacion de una posicion
del list[4]
print(list)
print(len(list))

"""
Podemos incluir el numero posicional en negativo, esto
nos es util para re-ordenar la lista o recorrer esta en inversa
"""

#agregar un elemento al final de la lista
list.append(7)

#agregar un elemento donde nosotros especifiquemos
list.insert(0, 100)
#el primer argumento es la posicion
#el segundo es el valor

#una forma de intercambiar posiciones
#my_list[0], my_list[4] = my_list[4], my_list[0]