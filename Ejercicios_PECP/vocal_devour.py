#Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales!
result = ""
vocal = "AEIOU"
#upper transforma cada letra de un str a mayusculas
user_word = input("Ingrese una palabra: ").upper()

#Si usamos el for asi podemos recorrer una cadena de texto
for i in user_word:
    #Valoramos letra por letra si esta es una vocal
    if i in vocal:
        continue
    else:
        print(i)
