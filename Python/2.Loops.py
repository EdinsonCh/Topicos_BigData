print("Estructuras repetitivas en Python")

# For
for i in range(1,11):
    print(f'Número {i}')

for letra in ("Hola mundo"):
    print(letra)

# While
contador = 1
while contador <=3:
    print(f'Intento {contador}')
    contador += 1 # contador = contador + 1

#Do While
# No existe en Python, pero se puede simular con un bucle while y una condición de salida
while True:
    numero = int(input("Ingrese un número > 0: "))
    if numero > 0:
        break


