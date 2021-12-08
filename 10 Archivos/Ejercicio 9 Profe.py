'''Partiendo de la siguiente lista de tuplas, donde cada tupla contiene el nombre de un estudiante y la nota obtenida.
alumnos = [('David', 5), ('Irene', 9), ('Maria', 6.5), ('Antonio',4.2), ('Marta', 3.7)]
Escribir un programa que guarde en un archivo de texto notas.txt el nombre de cada alumno junto con su nota en una linea de texto.
Cerrar el archivo y posteriormente deberá abrirlo para leer su contenido y volver a cerrarlo.'''

#Creamos una lista de tuplas con el nombre de un estudiante y la nota obtenida.
alumnos = [('David', 5), ('Irene', 9), ('Maria', 6.5), ('Antonio',4.2), ('Marta', 3.7)]

#Abrimos el archivo de texto en modo escritura
with open("notas.txt", "w") as f:

    #Recorremos la lista de tuplas
    for nombre, nota in alumnos:

       #Escribimos el nombre de cada alumno junto con su nota en una linea
       #separados ambos por un guión.
       f.write(nombre + " - " + str(nota) + "\n")


#Abrimos el archivo de texto en modo escritura
with open("notas.txt", "r") as f:

    #Recorremos todas las lineas del archivo
    for linea in f.readlines():
        #La imprimimos
        print(linea)
