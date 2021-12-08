"""
Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de una persona y
que calcule su índice de masa corporal (imc).
Se recuerda que el imc se calcula con la fórmula imc = peso / altura 2

2.bis) Vamos a modificar el programa del ejercicio 2. Ademas de mostrarnos nuestra masa corporal,
en función de la misma nos mostrara uno de los siguientes mensajes:.

Mensaje: Índice de masa corporal (IMC)
Peso inferior al normal Menos de 18.5
Peso Normal 18.5 – 24.9
Peso superior al normal 25.0 – 29.9
Obesidad Más de 30.0
"""

#PSEUDOCODIGO
#INICIO Indice de masa corporal
#ESCRIBIR Informacion que haga el programa
#LEER Numero de peso
#LEER Numero de altura
#CALCULAR
#ESCRIBIR Resumen y el resultado
#FIN



#import module for clearing the screen
import os
#About
os.system('clear')#this is only for Linux
#Orden sequencial
print('-------------------------------------------------------------------------------')
print("Programa calcula Indice de masa corporal(IMC) \nen ingles body mass index (BMI), de la altura y peso.")
print('-------------------------------------------------------------------------------')
#Input data from the user
nPeso = float(input('Escriba el peso en kilogramos:'))
nAltura = float(input('Escriba la altura en metros:'))
#Calcualtions (kg/metros)
BMI = round(nPeso / (nAltura **2),2)
#Output
print('Índice de masa corporal (IMC):')
#Orden selectiva
if BMI < 18.5 and BMI > 0 :
    message = 'Tiene IMC de',BMI,'que es peso inferior al normal.'
elif BMI >= 18.5 and BMI <= 24.9 :
    message = 'Tiene IMC de',BMI,'que es peso normal.'
elif BMI >= 25.0 and BMI <= 29.9 :
    message = 'Tiene IMC de',BMI,'que es peso superior.'
elif BMI >= 30 :
    message = 'Tiene IMC de',BMI,'que es obesidad.'
elif BMI <= 0 :
    message = 'Tu has indicado los datos malos seguramente.'
else:
    message = 'Un error, felicidades!'
print(message)