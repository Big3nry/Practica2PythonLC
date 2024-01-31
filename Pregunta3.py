numeros = []
while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()
    if respuesta == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
    elif respuesta == "NO":
        break
    else:
        print("Respuesta no válida. Por favor, ingrese 'SI' o 'NO'.")
print("Números ingresados:", numeros)
num_pares = 0
num_impares = 0
for num in numeros:
    if num % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1
print("Cantidad de números pares:", num_pares)
print("Cantidad de números impares:", num_impares)