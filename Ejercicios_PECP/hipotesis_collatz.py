c0 = int(input("Ingrese número mayor a 0: "))
cont = 0
if c0 > 0:
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 / 2
        else:
            c0 = 3 * c0 +1
        cont += 1
        print(c0)
    print(f"Pasos = {cont}")
else:
    print("El numero ingresado no es válido...")
