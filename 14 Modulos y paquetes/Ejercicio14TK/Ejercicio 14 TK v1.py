'''
Vamos a crear una aplicación para una clínica veterinaria para llevar el control de sus
pacientes.

Los datos de la mascota serán los siguientes: nombre, especie, raza, sexo, fecha de nacimiento
y número de PET PASSPORT.

Crearemos una función que devuelve la edad actual de la mascota, restando de la fecha actual
la fecha de nacimiento de la mascota.

El dato sexo tiene que ser validado, solo se admitirá M para masculino y F para femenino.
El dato fecha de nacimiento tiene que ser validado. La forma correcta será dd/mm/aaaa.
El dato número de PET PASSPORT tiene que ser validado. En la Unión Europea, el pasaporte
para mascotas empieza con el código del país (para España: ES) seguido de nueve dígitos. Para
validarlo tenemos que comprobar que empiece por ES y que contenga nueve dígitos (Ejemplo
ES040320011)
Las funciones para validar el sexo, la fecha y el número de PET PASSPORT estarán incluidas
dentro de un módulo llamado validador.
La función que calcula la edad de la mascota estará en otro modulo.
'''

#import module for clearing the screen
import os
import Ejercicio14_validator as validator
import Ejercicio14_validate_age as getage

#About
os.system('clear')#this is only for Linux, if this code fails in Windows, put it in comment
print('-------------------------------------------------------------------------------')
print("Programa para una clinica veterinaria o carniceria. version 0.1")
print('-------------------------------------------------------------------------------')

#Functions are in separate modules

def main():
    ''''''
    print('Clinica veterinaria de mascotas.')
    print('Rellene la ficha de la mascota')

    species = input('Especie(gato, perro, pato, rata..):')
    name =  input('Nombre(pupu, nufu, Oscar, perrito, etc):')
    breed = input('Raza(normal, especial, etc):')
    sex = validator.validateInput(input('Sexo (M/F):'))
    birthdate = validator.validateBirthDates(input('Fecha de nacimiento en formato dd/mm/yyyy:')) #store the data in format dd/mm/yyyy
    passport = validator.validatePassport(input('número de PET PASSPORT:'))

    age = getage.age(birthdate)
    birthdate = birthdate.strftime('%d-%m-%Y')

    print('----------------------RESUMEN--------------------------------')
    print('Nombre de pokemon:',name)
    print('Especie:', species)
    print('Raza:', breed)
    print('Sexo: ', sex)
    print('Fecha de nacimiento:',birthdate )
    print('PET PASSPORT numero: ',passport)
    print('Edad: ',age,'ano/s.')

#Program Start
if __name__ == '__main__':
    main()