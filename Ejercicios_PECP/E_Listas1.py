"""
Escenario
Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4, y 5.

Tu tarea es:

escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (Paso 1)
escribir una línea de código que elimine el último elemento de la lista (Paso 2)
escribir una línea de código que imprima la longitud de la lista existente (Paso 3).
"""

hat_list = [1, 2, 3, 4, 5]

hat_list[2] = int(input("Ingrese un nuevo valor para el del medio: "))
print(hat_list)

del hat_list[-1]
print(hat_list)

print(len(hat_list))