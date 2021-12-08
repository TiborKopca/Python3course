'''
El cociente de una división se calcula en Python con el operador //.
El resultado es siempre un número entero, pero será de tipo entero o decimal
dependiendo del tipo de los números empleados (en caso de ser decimal,
la parte decimal es siempre cero).

'''

print('10 // 3 = ',10 // 3) #3
print('10 // 4 = ',10 // 4) #2
print('20.0 // 7 = ',20.0 // 7) #2.0
print('20 // 6.0 = ',20 // 6.0) #3.0

'''
El resto de una división se calcula en Python con el operador %.
El resultado tendrá tipo entero o decimal,
de acuerdo con el resultado de la operación.
El operador resto % tiene la misma prioridad que la división.
'''
print('10 % 3 = ',10 % 3)   #1
print('10 % 4 = ',10 % 4)   #2
print('10 % 5 = ',10 % 5)   #0
print('10.5 % 3 = ', 10.5 % 3)  #1.5


#La función integrada divmod(x, y) devuelve una tupla formada por el cociente y el resto de la división de x entre y.
print('divmod(13, 4) ', divmod(13, 4))  #(3,1) 13/4 => 12/4 => 3, and the rest = 1

'''
Las potencias se calculan con el operador **, teniendo en cuenta que x ** y = xy.

Las potencias tienen prioridad sobre las multiplicaciones y divisiones.
'''
print('2 ** 3 = ', 2 ** 3)  #8

#También se pueden calcular potencias mediante la función integrada pow(x,y)
print('pow(2, 3) = ',pow(2, 3)) #8


#Para redondear un número (por ejemplo, cuando se muestra al usuario el resultado final de un cálculo),
#se puede utilizar la función integrada round().
#La función integrada round() admite uno o dos argumentos numéricos.
#Si sólo hay un argumento, la función devuelve el argumento redondeado al entero más próximo:

print(round(4.35))  #4

#Si el segundo argumento es positivo, el primer argumento se redondea con el número de decimales indicado:

print(round(4.3527, 2)) #4.35

#La función integrada abs() calcula el valor absoluto de un número, es decir, el valor sin signo.

print(abs(-6))  #6

#La función integrada max() calcula el valor máximo de un conjunto de valores (numéricos o alfabéticos).
#En el caso de cadenas, el valor máximo corresponde al último valor en orden alfabético,
#sin importar la longitud de la cadena.Las vocales acentuadas,
#la letra ñ o ç se consideran posteriores al resto de vocales y consonantes


print(max(4, 5, -2, 8, 3.5, -10))   #8
print(max("David", "Alicia", "Tomás", "Emilio"))    #Tomas
print(max("Ángeles", "Roberto"))      #Angeles, because first occurence of the result is Angeles

#La función integrada min() calcula el valor mínimo de un conjunto de valores (numéricos o alfabéticos).
#En el caso de cadenas,
#el valor mínimo corresponde al primer valor en orden alfabético,
#sin importar la longitud de la cadena.
#Las vocales acentuadas, la letra ñ o ç se consideran posteriores al resto de vocales y consonantes

print(min(4, 5, -2, 8, 3.5, -10)) #-10
print(min("David", "Alicia", "Tomás", "Emilio"))    #Alicia
print(min("Ángeles", "Roberto"))    #Roberto


#La función integrada sum() calcula la suma de un conjunto de valores.
#El conjunto de valores debe ser un tipo de datos iterable (tupla, rango, lista, conjunto o diccionario).
myTupla = (1, 2, 3, 4, 5)
print(sum(myTupla))         #15

#La función integrada sorted() ordena un conjunto de valores.
#El conjunto de valores debe ser un tipo de datos iterable (tupla, rango, lista, conjunto o diccionario).
#El conjunto de valores no se modifica, la función devuelve una lista con los elementos ordenados.
myLista = [10, 2, 8, -3, 6]
print(sorted(myLista))  #[-3,2,6,8,10]


