#Un bucle for es un bucle que repite el bloque de instrucciones un número prederminado de veces.
#El bloque de instrucciones que se repite se suele llamar cuerpo del bucle
#y cada repetición se suele llamar iteración.

'''No es necesario definir la variable de control antes del bucle,
aunque se puede utilizar como variable de control una variable ya definida en el programa.'''

'''El cuerpo del bucle se ejecuta tantas veces como elementos tenga el elemento recorrible
(elementos de una lista o de un range(), caracteres de una cadena, etc.). '''

print('Ejemplo 1')
print("Comienzo")
for i in [0, 1, 2]:
    print("Hola ", end="")
print()
print("Final")
print('----------------------')

'''Si la lista está vacía, el bucle no se ejecuta ninguna vez.'''

print('Ejemplo 2')
print("Comienzo")
for i in []:
    print("Hola ", end="")
print()
print("Final")
print('----------------------')

'''En el primer ejemplo, los valores que toma la variable no son importantes,
lo que importa es que la lista tiene tres elementos y por tanto el bucle se ejecuta tres veces.
El siguiente programa produciría el mismo resultado que el anterior:'''

print('Ejemplo 3')
print("Comienzo")
for i in [1, 1, 1]:
    print("Hola ", end="")
print()
print("Final")
print('----------------------')

'''Si la variable de control no se va a utilizar en el cuerpo del bucle, como en los ejemplos anteriores,
se puede utilizar el guion (_) en vez de un nombre de variable.
Esta notación no tiene ninguna consecuencia con respecto al funcionamiento del programa,
pero sirve de ayuda a la persona que esté leyendo el código fuente,
que sabe así que los valores no se van a utilizar. '''

'''El indicador puede incluir cualquier número de guiones bajos (_, __, ___, ____, etc).
Los más utilizados son uno o dos guiones'''

print('Ejemplo 4')
print("Comienzo")
for _ in [0, 1, 2]:
    print("Hola ", end="")
print()
print("Final")
print('----------------------')

'''En los ejemplos anteriores, la variable de control "i" no se utilizaba en el bloque de instrucciones,
pero en muchos casos sí que se utiliza.
Cuando se utiliza, hay que tener en cuenta que la variable de control
va tomando los valores del elemento recorrible. '''

print('Ejemplo 5')
print("Comienzo")
for i in [3, 4, 5]:
    print(f"Hola. Ahora i vale {i} y su cuadrado {i ** 2}")
print("Final")
print('----------------------')

'''La lista puede contener cualquier tipo de elementos, no sólo números.
El bucle se repetirá siempre tantas veces como elementos tenga la lista
y la variable irá tomando los valores de uno en uno. '''

print('Ejemplo 6')
print("Comienzo")
for i in ["Alba", "Benito", 27]:
    print(f"Hola. Ahora i vale {i}")
print("Final")
print('----------------------')

'''La costumbre más extendida es utilizar la letra i como nombre de la variable de control,
pero se puede utilizar cualquier otro nombre válido. '''

print('Ejemplo 7')
print("Comienzo")
for numero in  [0, 1, 2, 3]:
    print(f"{numero} * {numero} = {numero ** 2}")
print("Final")
print('----------------------')

'''La variable de control puede ser una variable empleada antes del bucle.
El valor que tuviera la variable no afecta a la ejecución del bucle,
pero cuando termina el bucle,
la variable de control conserva el último valor asignado'''

print('Ejemplo 8')
i = 10
print(f"El bucle no ha comenzado. Ahora i vale {i}")

for i in [0, 1, 2, 3, 4]:
    print(f"{i} * {i} = {i ** 2}")

print(f"El bucle ha terminado. Ahora i vale {i}")
print('----------------------')

'''Cuando se escriben dos o más bucles seguidos,
la costumbre es utilizar el mismo nombre de variable
puesto que cada bucle establece los valores de la variable
sin importar los valores anteriores'''

print('Ejemplo 9')
for i in [0, 1, 2]:
    print(f"{i} * {i} = {i ** 2}")

print()

for i in [0, 1, 2, 3]:
    print(f"{i} * {i} * {i} = {i ** 3}")

print()
print('----------------------')

'''En vez de una lista se puede escribir una cadena,
en cuyo caso la variable de control va tomando
como valor cada uno de los caracteres'''

print('Ejemplo 10')
for i in "AMIGO":
    print(f"Dame una {i}")
print("¡AMIGO!")
print('----------------------')

'''En los ejemplos anteriores se ha utilizado una lista
para facilitar la comprensión del funcionamiento de los bucles pero,
si es posible hacerlo, se recomienda utilizar tipos range(),
entre otros motivos porque durante la ejecución del programa
ocupan menos memoria en el ordenador.'''

#La función range() devuelve una secuencia de números,
#comenzando desde 0 de forma predeterminada,
#se incrementa en 1 (de forma predeterminada)
#hasta el número que se pasa como parámetro menos 1.
#En este ejemplo i valdra 0,1,2

print('Ejemplo 11')
print("Comienzo")
for i in range(3):
    print("Hola ", end="")
print()
print("Final")
print('----------------------')

#Se pueden pasar hasta tres parámetros separados por coma, donde el primer es el
#inicio de la secuencia, el segundo el final y el tercero el salto que se
#desea entre números.

print('Ejemplo 12')
print("Comienzo")
for i in range(3,12,2):
    print(i, end=",")
print()
print("Final")
print('----------------------')

'''Otra de las ventajas de utilizar tipos range() es que el argumento del tipo range()
controla el número de veces que se ejecuta el bucle.
Esto permite que el número de iteraciones dependa del desarrollo del programa.
En el ejemplo siguiente es el usuario quien decide cuántas veces se ejecuta el bucle'''

print('Ejemplo 13')
veces = int(input("¿Cuántas veces quiere que le salude? "))
for i in range(veces):
    print("Hola ", end="")
print()
print("Adiós")
print('----------------------')


#Se habla de bucles anidados cuando un bucle se encuentra en el
#bloque de instrucciones de otro bloque.
#Los bucles pueden tener cualquier nivel de anidamiento (un bucle
#dentro de otro bucle dentro de un tercero, etc.).
#Al escribir bucles anidados, hay que prestar atención al sangrado de las
#instrucciones, ya que ese sangrado indica a Python si una instrucción
#forma parte de un bloque u otro.

#En el ejemplo, el bucle externo (el controlado por i) se ejecuta 3 veces y el
#bucle interno (el controlado por j) se ejecuta dos veces por cada valor de i.

for i in range(3):
    for j in range(2):
        print(f"i vale {i} y j vale {j}")




