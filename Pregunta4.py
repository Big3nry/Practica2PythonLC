lista_alumnos = []
n = int(input("Ingrese la cantidad de alumnos: "))
for i in range(n):
    nombre_alumno = input(f"Ingrese el nombre del alumno {i + 1}: ")
    calificaciones = []
    for j in range(3):
        calificacion = float(input(f"Ingrese la calificación {j + 1} para {nombre_alumno}: "))
        calificaciones.append(calificacion)
    alumno = {
        'Alumno': nombre_alumno,
        'Notas': calificaciones
    }
    lista_alumnos.append(alumno)
print("\nListado completo de alumnos:")
for alumno in lista_alumnos:
    print(f"\nAlumno: {alumno['Alumno']}")
    print("Notas:", alumno['Notas'])