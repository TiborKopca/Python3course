'''
El Ministerio del Interior desea realizar una actualización del programa para la validación del
DNI español.
Hay que rehacer el programa del ejercicio 12 utilizando el paradigma de la programación
Modular.
Cada una de las funciones ira dentro de un módulo.
Se desarrollará una función nueva que tome el numero introducido por el usuario y lo devuelva
en MAYÚSCULAS con los espacios en blanco, los puntos, los guiones y los guiones bajos que el
usuario introduzca junto con el número del DNI ELIMINADOS.
El programa principal importara los módulos y ejecutara las funciones.
'''

#import module for clearing the screen
import os
import Ejercicio13_input_correctionTK as stripChars     #Import of the string correction
import Ejercicio13_character_count as test1             #Import of the number of characters test
import Ejercicio13_last_character as test2              #Import of the test of the last character
import Ejercicio13_select_numbers as getNumbers         #Import of the package to handle numbers
import Ejercicio13_validation_DNI as finalValidation    #Import of the last actual funcion to validate data
import Ejercicio13_userInput as input                   #user input functions

#About
os.system('clear')#this is only for Linux, if this code fails in Windows, put it in comment
print('-------------------------------------------------------------------------------')
print("Programa comprueba si la letra de un DNI introducido es correcta o no. \
En este utilizamos diseno modular, los paquetes son en otros ficheros.")
print('-------------------------------------------------------------------------------')

#Functions are in separate modules

def main():
    '''Recursive function to check the flow of the program for errors.'''
    inputDNI = input.userInput()                                     #input from the user

    inputDNI = stripChars.stripData(inputDNI)                        #we take out any unwanted characters from the input

    if inputDNI == '0':                                             #on 0 the program ends.
        print('El programa termina. Hasta pronto.')

    elif test1.checkLength(inputDNI):                               #checks for validity of Input data-if there is an error, error will be printed out and the program will be halted-sent to main()

        if test2.checkLastCharacter(inputDNI,letters):              #checks for validity of Input of the last Character, on error will go to main()

            numbersDNI = getNumbers.selectNumbers(inputDNI)         #store the 8 numbers in variable

            if numbersDNI != -1:                                    #if there was no exception

                indexOfLetter = finalValidation.letterIndexCalculation(numbersDNI)       #obtain index for the character list from the DNI
                calculatedCharacter = finalValidation.letterDNICalculated(indexOfLetter,letters)  #obtain letter from given DNI number

                inputDNICharacter = inputDNI[-1]                           #obtain last chararter from input
                resultBoolean = finalValidation.validateChars(calculatedCharacter,inputDNICharacter)     #final boolean validation
                if resultBoolean:                                   #Final results presention
                    print('El DNI es correcto.')
                else:
                    print('El DNI NO es correcto.')
                    print(f'La letra calculada de DNI introducido es:{calculatedCharacter}, pero la letra introducida es: {inputDNICharacter}.')
            else:
                main()                                                  #unexpected error with input data
        else:
            main()  #was error in test2 - last character test failed
    else:
        main()  #was error in test1 - count of DNI numbers not correct

#Variables
letters = ('T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E')


#Program Start
main()