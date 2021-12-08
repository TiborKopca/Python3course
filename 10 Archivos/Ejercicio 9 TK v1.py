'''
Partiendo de la siguiente lista de tuplas, donde cada tupla contiene el nombre de un estudiante y
la nota obtenida. alumnos = [('David', 5), ('Irene', 9), ('Maria', 6.5), ('Antonio',4.2), ('Marta', 3.7)]
Escribir un programa que guarde en un archivo de texto notas.txt el nombre de cada alumno junto
con su nota en una linea de texto. Cerrar el archivo y posteriormente deberá abrirlo para leer su
contenido y volver a cerrarlo.

'''
#import module for clearing the screen
import os
#About
os.system('clear')#this is only for Linux, if this code fails in Windows, put it in comment
print('-------------------------------------------------------------------------------')
print("Programa calcule la nota media del curso, el número de aprobados y el número de suspensos. Usa archivo 'notes.txt' para guardar datos.")
print('-------------------------------------------------------------------------------')

#VARIABLES
listaAlumnos = [('David', 5), ('Irene', 9), ('Maria', 6.5), ('Antonio',4.2), ('Marta', 3.7)]
notaMedia = 0
numberOfNotes = 0
notaTotal = 0
note = 0.0
numeroAprobados = 0
numeroSuspensos = 0
line = '-------------------------------------------------------------------------------'
fileStudents = 'Ejercicio9_notas.txt'

#INPUT
limite = float(input('Escribe desde cual nota seran aprobados:'))

#Open the file
fileWrite = open(fileStudents,'w')

for eachTuple in listaAlumnos:
    name, note = eachTuple

    #Writing each student as a line
    fileWrite.write('Nombre + Nota de alumno')
    fileWrite.write(name + ' ')
    fileWrite.write('')
    fileWrite.write(str(note))
    fileWrite.write('\n')

    notaTotal += note
    numberOfNotes += 1
    if note < limite:
        numeroAprobados += 1
    else:
        numeroSuspensos += 1

#Closing file
fileWrite.close()

notaMedia = notaTotal / numberOfNotes

print(line)

#Reading from the file
fileReadOnly = open(fileStudents, 'r')
print(fileReadOnly.read())  #output to the screen/terminal

print('Nota media es:',notaMedia)
print(f'Numero de aprobados es: {numeroAprobados}, y suspendidos: {numeroSuspensos}.')

#Closing file
fileReadOnly.close()




