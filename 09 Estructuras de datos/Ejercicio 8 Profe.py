'''Partiendo de la siguiente lista de tuplas, donde cada tupla contiene el nombre de un estudiante y la nota obtenida.
alumnos = [('David', 5), ('Irene', 9), ('Maria', 6.5), ('Antonio',4.2), ('Marta', 3.7)]
Escribir un programa que calcule la nota media del curso, el número de aprobados y el número de suspensos'''

#Creamos una lista de tuplas con el nombre de un estudiante y la nota obtenida.
alumnos = [('David', 5), ('Irene', 9), ('Maria', 6.5), ('Antonio',4.2), ('Marta', 3.7)]

#Creamos e inicializamos las variables
suma = 0
aprobados = 0
suspensos = 0

#Recorremos la listA
for nombre, nota in alumnos:
    #Sumamos las notas
    suma += nota

    #Sumamos los aprobados y los suspensos
    if nota >= 5:
        aprobados += 1
    else:
        suspensos += 1

#Presentamos los datos en pantalla
print(alumnos)
print()
print()
print("Nota media de la clase: ", suma/len(alumnos))
print("Número de aprobados: ", aprobados)
print("Número de suspensos: ", suspensos)
        

