'''PROGRAMACIÓN MODULAR'''

'''
Vamos a comparar entre la programación modular y la POO
para ello vamos a resolver un mismo problema utilizando
ambos paradigmas.
'''

#Creamos una extructura de datos
#Tres diccionarios que contienen el nivel de energia para un
#elefante, un leon y un loro.
elefante = {'energia': 50}
leon = {'energia': 5}
loro ={'energia': 70}

#Creamos una función que nos devuelve la energia del animal
def energia(animal):
    return animal['energia']

#Creamos una función que nos devuelve si el animal tiene sueño
def sueño(animal):
    if animal['energia'] < 10 :
        sueño = 'Tiene sueño'
    else:
        sueño = 'No tiene sueño'
    return sueño
    





