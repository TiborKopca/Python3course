#Python distingue entre números enteros y decimales.
#Al escribir un número decimal, el separador entre la parte entera y la parte decimal es un punto.

numeroEntero = 4
numeroDecimal =2.5

'''
Si se escribe una coma como separador entre la parte entera y la decimal,
Python no lo entiende como separador,
sino como una pareja de números (concretamente, lo entiende como una tupla de dos elementos).
'''
numeroDecimalIncorrecto = 8,6

for i in numeroDecimalIncorrecto:
    print("Valor tupla: ", i)


#Si se escribe un número con parte decimal 0, Python considera el número como número decimal.

numeroDecimal =2.0

#Se puede escribir un número decimal sin parte entera, pero lo habitual es escribir siempre la parte entera.

numeroDecimal =.5

#Al sumar, restar o multiplicar números enteros y decimales, el resultado es siempre decimal.
#En el caso de que el resultado no tenga parte decimal,
#Python escribe 0 como parte decimal para indicar que el resultado es un número decimal.

print('4.5 * 3 = ', 4.5 * 3)
print('4.5 * 2 = ', 4.5 * 2)

#Al sumar, restar o multiplicar números enteros, el resultado es entero.

print('1 + 2 = ',1 + 2)
print( '3 - 4 = ',  3 - 4)
print('5 * 6 = ', 5 * 6)

#Al dividir números enteros, el resultado es siempre decimal, aunque sea un número entero.
#Cuando Python escribe un número decimal, lo escribe siempre con parte decimal, aunque sea nula.

print('9 / 2 = ',9 / 2)
print('9 / 3 = ', 9 / 3)

#Dividir por cero genera un error:

#5/0

'''
Cuando en una fórmula aparecen varias operaciones,
Python las efectúa aplicando las reglas usuales de prioridad de las operaciones
(primero multiplicaciones y divisiones, después sumas y restas).
'''

print('1 + 2 * 3 = ',1 + 2 * 3)
print('10 - 4 * 2 = ',10 - 4 * 2)

#En caso de querer que las operaciones se realicen en otro orden, se deben utilizar paréntesis.
print('(5 + 8) / (7 - 2) = ',(5 + 8) / (7 - 2)) 












