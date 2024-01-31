meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

def convertir_fecha(input_fecha):
    partes_fecha = input_fecha.split()

    if '/' in partes_fecha[0]:
        mes, dia, anio = map(int, partes_fecha[0].split('/'))
    else:
        mes = meses.index(partes_fecha[0]) + 1
        dia = int(partes_fecha[1][:-1])  
        anio = int(partes_fecha[2])
    fecha_formateada = f"{anio:04d}-{mes:02d}-{dia:02d}"
    return fecha_formateada

input_fecha1 = input("Ingrese una fecha en formato mes-día-año (por ejemplo, 9/8/1636): ")
resultado1 = convertir_fecha(input_fecha1)
print("Fecha formateada:", resultado1)

input_fecha2 = input("Ingrese una fecha en formato mes día, año (por ejemplo, Septiembre 8, 1636): ")
resultado2 = convertir_fecha(input_fecha2)
print("Fecha formateada:", resultado2)