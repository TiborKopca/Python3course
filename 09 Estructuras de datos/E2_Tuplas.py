#Una tupla es una variable que permite almacenar varios datos diferentes que
#no pueden ser modificados una vez creados

#las tuplas son tipos inmutables, lo que significa que una vez asignado su valor, no puede ser modificado.
#Si se intenta,tendremos un TypeError.

tupla1 = (1, 2, 3)  # declara tupla (se usan paréntesis)...
tupla2 = 1, 2, 3  # ...aunque pueden declararse sin paréntesis

print('tupla1',tupla1) #tupla1 (1, 2, 3)
print('tupla2',tupla2) #tupla2 (1, 2, 3)

print('---------------------------------------------------------------------------------------')

#es posible crear una tupla de un solo elemento. Para ello debes usar , antes del paréntesis,
#porque de lo contrario (2) sería interpretado como int.
singleton = (2,)  # con un elemento hay terminar con “,”
print('singleton',singleton) #singleton (2,)

print('---------------------------------------------------------------------------------------')

#Al igual que las listas, las tuplas también pueden ser anidadas.
tupla4 = tupla1, 4, 5, 6  # anida tuplas
print('tupla4', tupla4) #tupla4 ((1, 2, 3), 4, 5, 6)
tupla5 = ()  # declara una tupla vacía
print('tupla5', tupla5) #tupla5 ()

print('---------------------------------------------------------------------------------------')

#Es posible crear una tupla a partir de los otros tipos de secuencia: listas
#o cadenas. Para esto haremos uso de la función tuple()
tupla6 = tuple([1, 2, 3, 4, 5])  # Convierte una lista en una tupla
print('tupla6', tupla6) #tupla6 (1, 2, 3, 4, 5)

range_tupla = tuple(range(4)) #Crea una tupla con range()
print('tupla con range',range_tupla) #mi_tupla (0, 1, 2, 3)

mi_cadena ="Hola mundo" #Crear una tupla desde una cadena
mi_tupla2 = tuple(mi_cadena)
print('mi_tupla2',mi_tupla2) #mi_tupla2 ('H', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o')

print('---------------------------------------------------------------------------------------')

#se puede también asignar el valor de una tupla con n elementos a n variables.
myTupla = (1, 2, 3)
x, y, z = myTupla
print(x, y, z) #1 2 3

print('---------------------------------------------------------------------------------------')

#Se puede iterar una tupla de la misma forma que se hacía con las listas.
tupla = ['a', 1, 'Lapiz', 2.5, 4, 5, 'arcoiris', 10]
tupla_tupla = ('a', 1, 'Lapiz', 2.5, 4, 5, 'arcoiris', 10)
print('tupla1 es',type(tupla))
print('tupla1 es',type(tupla_tupla))
print('tupla', tupla) #tupla ['a', 1, 'Lapiz', 2.5, 4, 5, 'arcoiris', 10]
for t in tupla2:
    print(t) #print value in each row

print('---------------------------------------------------------------------------------------')

# Seaccede a los valores desde:hasta
print('tupla[1:3]', tupla[1:3]) #tupla[1:3] [1, 'Lapiz']
print('tupla[3]' ,tupla[3])     #tupla[3] 2.5














