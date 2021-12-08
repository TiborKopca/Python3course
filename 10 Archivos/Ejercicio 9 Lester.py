#Partiendo de la siguiente lista de tuplas, donde cada tupla contiene el nombre de un estudiante y
#la nota obtenida. alumnos = [('David', 5), ('Irene', 9), ('Maria', 6.5), ('Antonio',4.2), ('Marta', 3.7)]
#Escribir un programa que guarde en un archivo de texto notas.txt el nombre de cada alumno junto
#con su nota en una linea de texto. Cerrar el archivo y posteriormente deberá abrirlo para leer su
#contenido y volver a cerrarlo.


#INICIO

alumnos = [('David', 5), ('Irene', 9), ('Maria', 6.5), ('Antonio',4.2), ('Marta', 3.7)]

f = open("notas.txt", "w")

for nombre, nota in alumnos:
    f.write(nombre + ": " + str(nota) + "\n")
f.close()
f = open("notas.txt", "r")
print(f.read())
f.close()

#FIN
