"""
En un laboratorio de ingeniería ha sido contratado por la NASA para evaluar la fiabilidad de un
componente particular para una futura sonda espacial enviada a Júpiter. Como parte de esta
evaluación, un ingeniero en su laboratorio probó varios de estos circuitos y registró el tiempo que
tardó cada uno en fallar. Ahora desea desarrollar un programa que procese estos datos y determine
el tiempo medio de fallo.

Presentar la siguiente documentación:
➔ ALGORITMO EN SEUDOCÓDIGO.
➔ ALGORITMO EN DIAGRAMA DE FLUJO.
➔ CODIFICACIÓN EN PYTHON
"""

#PSEUDOCODIGO
#INICIO Indice de polucion
#ESCRIBIR Informacion que haga el programa
#LEER 'Introduzca el cuantos cirquitos tienes:'
# MIENTRAS i <= nCirquitos:
#   LEER 'Introduzca los horas hasta que ha fallado el cirquito {i}
#   nTiempo += nInput
# FIN_MIENTRAS
# nTiempoFinal = nTiempo/nCirquitos
#ESCRIBIR nTiempoFinal
#FIN

#import module for clearing the screen
import os
#About
os.system('clear')#this is only for Linux
print('-------------------------------------------------------------------------------')
print("Programa determine el tiempo medio de fallo de los componentes dados.")
print('-------------------------------------------------------------------------------')

#Inicializacion de variables
i = 1
nTiempo = 0
message = 'El tiempo medio de fallo de los componentes dados es:'
nCirquitos = " "

#Input data from the user
while not nCirquitos.isdigit(): #isdigit() == true if all the characters are digits
    #print('No es un integer.')
    nCirquitos = input('Introduzca el cuantos cirquitos tienes(numero positivo):')

nCirquitos = int(nCirquitos)

#Repetitiva Mientras (while)
while i <= nCirquitos:
    nInput = float(input(f'Introduzca los horas hasta que ha fallado el cirquito {i}:'))
    nTiempo += nInput               #the time entered we add to the total time
    print('Tiempo total:',nTiempo)
    i += 1

#Calcualtions
nTiempoFinal = nTiempo/nCirquitos   #time of the all components / number of components
#Output
print(message,nTiempoFinal,'horas')
