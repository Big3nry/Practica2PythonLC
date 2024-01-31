def omitir_vocales(cadena):
    cadena_sin_vocales = ''.join(letra for letra in cadena if letra.lower() not in 'aeiouAEIOU')
    return cadena_sin_vocales

cadena_usuario = input("Ingrese una cadena de texto: ")

resultado = omitir_vocales(cadena_usuario)
print("Cadena con vocales omitidas:", resultado)