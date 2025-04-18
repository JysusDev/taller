# Con un ciclo for imprima los numeros impares
for i in range(1, 11):
    if i % 2 != 0:
        print(i)

# Con un ciclo while imprima los numeros impares
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1

# Cuando llegue el @ salga del ciclo e imprima todo lo anterior a el
plb = ""
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    else:
        plb += ch
print (plb)

for digit in "0165031806510":
    if digit == "0":
        print( "x" )
        continue
    print (digit)

n = 3
 
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)
    