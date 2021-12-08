'''
Partiendo de la siguiente lista de tuplas, donde cada tupla contiene el nombre de un estudiante y
la nota obtenida.
alumnos = [('David', 5), ('Irene', 9), ('Maria', 6.5), ('Antonio',4.2), ('Marta', 3.7)]
Escribir un programa que calcule la nota media del curso, el número de aprobados y el número de
suspensos.
'''
#import module for clearing the screen
import os
#About
os.system('clear')#this is only for Linux, if this code fails in Windows, put it in comment
print('-------------------------------------------------------------------------------')
print("Programa calcule la nota media del curso, el número de aprobados y el número de suspensos.")
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

#INPUT
limite = float(input('Escribe desde cual nota seran aprobados:'))

for eachTuple in listaAlumnos:
    name, note = eachTuple
    notaTotal += note
    numberOfNotes += 1
    if note < limite:
        numeroAprobados += 1
    else:
        numeroSuspensos += 1

notaMedia = notaTotal / numberOfNotes

print(line)
print('Nota media es:',notaMedia)
print(f'Numero de aprobados es: {numeroAprobados}, y suspensos: {numeroSuspensos}.')




