'''
Una variable se puede entender como una especie de caja en la que se puede guardar un valor (por ejemplo, un valor numérico).
Esa caja suele corresponder a una posición de memoria en la memoria del ordenador.
Las variables se representan también mediante letras o palabras completas: x, y, a, b, nombre, apellidos, edad, etc.
Cuando en esos lenguajes de programación escribimos la instrucción
'''

a = 2

'''
 lo que estamos pidiendo al programa es que guarde el valor 2 en una "caja" y que a la caja le llame a.

En esos lenguajes, el símbolo igualdad (=) hay que entenderlo como una asignación,
no como una igualdad matemática. Al escribir una igualdad,
le estamos pidiendo al programa que calcule lo que hay a la derecha de la igualdad
y que lo guarde en la variable que hay a la izquierda de la igualdad.

Una vez hemos guardado un valor en una variable,
podemos hacer referencia a él a lo largo del programa.
Por ejemplo, el siguiente programa
'''

a = 2
b = 3
c = a + b

'''
guarda el valor 2 en la variable a
guarda el valor 3 en la variable b
coge los valores guardados en las variables a y b (2 y 3), los suma (2+3) y el resultado (5) lo guarda en la variable c.
'''

#reverse the values in variables without third temporary variable
print('-----------------------------')
a=7
print('a1',a)
b=9
print('b1',b)
print('reversed values in variables')
a=a+b #16 = 7+9
b=a-b #7 = 16-9
a=a-b #9 = 16-7
print('a2',a)
print('b2',b)