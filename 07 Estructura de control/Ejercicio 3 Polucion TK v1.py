"""""
El nivel de polución del aire en la ciudad de Manacor. Se hacen lecturas en tres puntos distintos a
las 12PM en la estación del tren, en el centro de la ciudad y en un lugar seleccionado al azar en un d
área residencial. La media de las tres lecturas es el índicee polución y un valor de 50 o más
significa situación peligrosa, mientras que valores por debajo de 50 significa situación segura.
Debido a que el índice debe calcularse diariamente, el estadístico medioambiental de Manacor
desea un programa que calcule el índice de polución y determine la situación en ese momento segura o peligrosa.

Presentar la siguiente documentación:
➔ ALGORITMO EN SEUDOCÓDIGO.
➔ ALGORITMO EN DIAGRAMA DE FLUJO.
➔ CODIFICACIÓN EN PYTHON.
"""
#PSEUDOCODIGO
#INICIO Indice de polucion
#ESCRIBIR Informacion que haga el programa
#LEER Numero de lectura de la ciudad
#LEER Numero de lectura de tren
#LEER Numero de lectura de residencial
#SI (nCentro + nEstacion + nResidencial)/3 <= 50) ENTONCES
#   message = 'segura'
#SI_NO ENTONCES
#   message = 'peligrosa'
#FIN_SI
#ESCRIBIR Resumen y el resultado
#FIN

#import module for clearing the screen
import os
#About
os.system('clear')#this is only for Linux
print('-------------------------------------------------------------------------------')
print("Programa calcule el índice de polución y determine la situación en ese momento segura o peligrosa.")
print('-------------------------------------------------------------------------------')

#Input data from the user
nCentro = float(input('Ecribe la lectura del centro de la ciudad:'))
nEstacion = float(input('Ecribe la lectura en la estación del tren:'))
nResidencial = float(input('Ecribe la lectura en un área residencial:'))

#Calcualtions
message = ''
if((nCentro + nEstacion + nResidencial)/3 <= 50):
    message = 'segura.'
else:
    message = 'peligrosa.'
#Output
print('La situacion es',message)
#print((nCentro + nEstacion + nResidencial)/3)