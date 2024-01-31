def factorial(numero):
    if numero == 0:
        return 1
    elif numero < 0:
        return "Error: El factorial no está definido para números negativos"
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

numero_ingresado = int(input("Ingrese un número para calcular su factorial: "))

print(f"El factorial de {numero_ingresado} es: {factorial(numero_ingresado)}")
