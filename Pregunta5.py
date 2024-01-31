def contar_digitos(numero, digito):
    numero_str = str(numero)
    cantidad = numero_str.count(str(digito))

    return cantidad
numero_ingresado = 15789000
digito_solicitado = 0
resultado = contar_digitos(numero_ingresado, digito_solicitado)
print(f"Cantidad de veces {digito_solicitado} en el número: {resultado}")