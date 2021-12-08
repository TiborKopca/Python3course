'''
Vamos a comparar entre la programación modular y la POO
para ello vamos a resolver un mismo problema utilizando
ambos paradigmas.
'''

#Importamos el modulo con las funciones y los datos
from animalModulos import *

#Importamos la Clase animalClase
from animalClase import *

print('PROGRAMACIÓN MODULAR')
#Ejecutamos las funciones
print('El Leon tiene', energia(leon), 'de energia')
print('El Leon', sueño(leon))

print('El Elefante tiene', energia(elefante), 'de energia')
print('El Elefante', sueño(elefante))
      
print('El Loro tiene', energia(loro), 'de energia')
print('El Loro', sueño(loro))

print('____________________________________________________________')


print('PROGRAMACIÓN ORIENTADA A OBJETOS')
#Creamos los objetos Leon, Elefante y Loro
#Al crear los objetos introducimos los datos (la energia de cada objeto)
#Los datos (propiedades o atributos) y las funciones (metodos) van juntos
#dentro de la clase
Leon = Animal(5)
Elefante = Animal(50)
Loro = Animal(8)

#Podemos crear todos los objetos que se nos ocurran.
Pato = Animal(5)
Gatito = Animal(10)

print('El Leon tiene',Leon.getEnergia() , 'de energia')
print('El Leon', Leon.sueño())

print('El Elefante tiene', Elefante.getEnergia(), 'de energia')
print('El Elefante', Elefante.sueño())

print('El Loro', Loro.getEnergia(), 'de energia')
print('El Loro', Loro.sueño())
      
print('El Pato tiene',Pato.getEnergia(), 'de energia')
print('El Pato', Pato.sueño())

print('El Gatito tiene',Gatito.getEnergia(), 'de energia')
print('El Gatito', Gatito.sueño())

