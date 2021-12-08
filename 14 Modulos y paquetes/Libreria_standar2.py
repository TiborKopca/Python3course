'''math: módulo que añade funciones matemáticas'''

'''
El módulo math te permitirá incluir en tus programas funciones y
constantes matemáticas para facilitarte aquellos desarrollos que
realices que requieran operaciones matemáticas complejas.
'''
import math

#retorna el valor absoluto del número especificado como parámetro
print("El valor absoluto de -7 es: ", math.fabs(-7))    #El valor absoluto de -7 es:  7.0

#calcula la factorial del número especificado como parámetro
print("El factorial de 9 es: ", math.factorial(9))  #El factorial de 9 es:  362880

#calcula el máximo común divisor de dos números especificados como parámetros

#La función retornará False en caso de que sea un número y True en caso contrario.
print("isnan(8): ",math.isnan(8))       #isnan(8):  False

#calcula el logaritmo en base X del número especificado como parámetro.
print("El logaritmo en base 10 de 540 es: ", math.log(540,10))  #El logaritmo en base 10 de 540 es:  2.7323937598229686

#calcula la potencia del número especificado como parámetro.
print("El valor de 2 elevado a 10 es: ", math.pow(2,10))    #El valor de 2 elevado a 10 es:  1024.0

#calcula la raíz cuadrada del número especificado como parámetro.
print("La raiz cuadrada de 144 es: ", math.sqrt(144))       #La raiz cuadrada de 144 es:  12.0

#retorna el valor en grados del ángulo en radianes recibido como parámetro.
print("El ángulo 1.57 en grados es: ", math.degrees(1.57))  #El ángulo 1.57 en grados es:  89.95437383553924

#retorna el valor en radianes del ángulo en grados recibido como parámetro.
print("El ángulo 90 en radianes es: ", math.radians(90))    #El ángulo 90 en radianes es:  1.5707963267948966

#calcula el seno en radianes del ángulo especificado como parámetro.

print("El seno de un ángulo de 180 es: ", math.sin(math.radians(180)))  #El seno de un ángulo de 180 es:  1.2246467991473532e-16

#calcula el coseno en radianes del ángulo especificado como parámetro.
print("El coseno de un ángulo de 180 es: ",
math.cos(math.radians(180)))    #El coseno de un ángulo de 180 es:  -1.0

#calcula la tangente en radianes del ángulo especificado como parámetro.
print("La tangente de un ángulo de 180 es: ",
math.tan(math.radians(180)))   #La tangente de un ángulo de 180 es:  -1.2246467991473532e-16

#calcula el arcoseno en radianes del ángulo especificado como parámetro.
print("El arcoseno de 1 es: ", math.degrees(math.asin(1))) #El arcoseno de 1 es:  90.0

#calcula el arcocoseno en radianes del ángulo especificado como parámetro.
print("El arcocoseno de 1 es: ", math.degrees(math.acos(1)))    #El arcocoseno de 1 es:  0.0

#calcula la arcotangente en radianes del ángulo especificado como parámetro.
print("La arcotangente de 1 es: ", math.degrees(math.atan(1)))  #La arcotangente de 1 es:  45.0

#el valor de la constante π.
print("El valor de pi es: ", math.pi)   #El valor de pi es:  3.141592653589793

#el valor de la constante e.
print("El valor de e es: ", math.e) #El valor de e es:  2.718281828459045

#el valor de la constante τ.
print("El valor de tau es: ", math.tau) #El valor de tau es:  6.283185307179586


