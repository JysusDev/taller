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

"""
Para copiar los elementos de una lista en
una nueva es necesario usar la siguiente
sintaxis

list2 = list[:] para la lista completa
[inicio:fin-1] para solo una parte
esto tambien lo podemos usar con del
del list[1:3]
"""

"""
in y not in
devuelven valores booleanos, los podemos usar
para saber si hay un elemento que nosotros 
especifiquemos en una lista
"""