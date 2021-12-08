'''random: módulo que permite realizar elecciones al azar.'''


'''
El módulo random va a permitirte hacer elecciones de forma aleatoria,
tanto elegir al azar un valor de una lista como generar números
aleatorios u obtener un número al azar dentro de un rango.
'''

import random


#Devuelve un número aleatorio en un rango especificado.
print("Número aleatorio(1-100): ",  random.randrange(100))

#Devuelve una lista de números aleatorios dentro de un rango establecido.
print('Lista aleatoria de seis números(1-50): ',random.sample(range(50), 6))



#Devuelve un número en coma flotante.
print("Número aleatorio en coma flotante: ",random.random())

#selecciona un elemento de la lista que recibe por parámetro al azar.
colores =['Rojo', 'Verde', 'Amarillo', 'Azul', 'Rosa']

print("Elección aleatoria [Rojo,Verde,Amarillo,Azul,Rosa]: ",
random.choice(colores))




