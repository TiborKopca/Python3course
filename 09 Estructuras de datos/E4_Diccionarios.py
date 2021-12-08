'''
Los diccionarios, también llamados matrices asociativas, deben su
nombre a que son colecciones que relacionan una clave y un valor.
Los pares clave-valor están separados por dos puntos, las parejas por
comas y todo el conjunto se encierra entre llaves.
'''
# declara diccionario
capitales = {
    'Chile'     :'Santiago',
    'España'    :'Madrid',
    'Francia'   :'París'}
print('capitales', capitales) #capitales {'Chile': 'Santiago', 'España': 'Madrid', 'Francia': 'París'}
print(capitales["Francia"]) #París

#También podemos crear un diccionario con la función dict()
# declara a partir de cadenas simples
mydiccionario = dict(
    Nombre          =           'Sara',
    Edad            =           27,
    Documento       =           1003882)
print('mydiccionario',mydiccionario) #mydiccionario {'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}

# declara a partir de tupla
d2 = dict([
      ('Nombre', 'Lourdes'),
      ('Edad', 61),
      ('Documento', 1003342),
      ])
print('d2', d2)
#d2 {'Nombre': 'Lourdes', 'Edad': 61, 'Documento': 1003342}


#Se puede acceder a sus elementos con [] o también con la función get()
print('La capital de Chile es', capitales['Chile']) #La capital de Chile es Santiago
print(d2.get('Nombre')) #Lourdes

#Para modificar un elemento basta con usar []
#con el nombre del key y asignar el valor que queremos.
#si se asigna un valor a una clave ya existente, se reemplaza el valor anterior

d2['Nombre'] = "Laura"
print(d2) #{'Nombre': 'Laura', 'Edad': 61, 'Documento': 1003342}

#Si el key al que accedemos no existe, se añade automáticamente.
d2['Direccion'] = "Calle 123"
print(d2) #'Nombre': 'Laura', 'Edad': 61, 'Documento': 1003342, 'Direccion': 'Calle 123'}

capitales['Portugal'] = 'Lisboa'  # agrega par Portugal:Lisboa
print(capitales) #{'Chile': 'Santiago', 'España': 'Madrid', 'Francia': 'París', 'Portugal': 'Lisboa'}

#Para comprobar la existencia de una clave podemos usar la función
#get() o el operador in
if 'Portugal' in capitales:
    print('Capital Portugal:', capitales['Portugal']) #Capital Portugal: Lisboa

if capitales.get('Portugal'):
   print('Capital Portugal:', capitales['Portugal']) #Capital Portugal: Lisboa


#Un diccionario permite eliminar cualquier entrada con la función: del()
del capitales['Francia']  # borra el par Francia:París

#Los diccionarios se pueden iterar de manera muy similar a las listas u otras estructuras de datos.
# Imprime los key del diccionario
print('Imprime los key del diccionario')
for x in capitales:
    print(x)    #will print in rows Chile, Espana, Portugal


# Impre los value del diccionario
print()
print('Imprime los valores del diccionario')
print()

for x in capitales:
    print(capitales[x]) #will print Santiago,Madrid,Lisboa

#Podemos mostrar los valores de manera más eficiente accediendo a los
#valores mediante values():
print()
print('Imprime los valores del diccionario mas eficientemente' )
print()

for x in capitales.values():
    print(x)             #will print Santiago,Madrid,Lisboa


# Imprime los key y value del diccionario
print()
print('Imprime los key y value del diccionario')
print()

for x in capitales:
    print(x,'==', capitales[x])
    #Chile == Santiago
    #España == Madrid
    #Portugal == Lisboa

#Disponemos de items() para mostrar tanto clave como valor de manera más eficiente
print()
print(' muestra tanto clave como valor de manera más eficiente')
print()

for x, y in capitales.items():
    print(x, y)
    #Chile Santiago
    #España Madrid
    #Portugal Lisboa




