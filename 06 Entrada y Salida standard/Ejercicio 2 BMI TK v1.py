"""
Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de una persona y
que calcule su índice de masa corporal (imc).
Se recuerda que el imc se calcula con la fórmula imc = peso / altura 2
"""
#import module for clearing the screen
import os
#About
os.system('clear')#this is only for Linux
print('-------------------------------------------------------------------------------')
print("Programa calcula Indice de masa corporal(IMC) \nen ingles body mass index (BMI), de la altura y peso.")
print('-------------------------------------------------------------------------------')
#Input data from the user
nPeso = float(input('Escriba el peso en kilogramos:'))
nAltura = float(input('Escriba la altura en metros:'))
#Calcualtions
BMI = round(nPeso / (nAltura **2),2)
#Output
print('El IMC de valores introducidos es',BMI)
print('')

#PSEUDOCODIGO
#INICIO Indice de masa corporal
#ESCRIBIR Informacion que haga el programa
#LEER Numero de peso
#LEER Numero de altura
#CALCULAR
#ESCRIBIR Resumen y el resultado
#FIN