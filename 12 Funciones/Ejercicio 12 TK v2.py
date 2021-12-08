'''
El Ministerio del Interior nos ha contratado para realizar un programa para la
validación del DNI español.
El programa tendrá las siguientes especificaciones:

✓ El usuario introducirá el número de su DNI con la letra en una sola entrada
(11111111A)

✓ Se comprobará si el número de caracteres introducido es el correcto, sabiendo
que el DNI tiene 9 caracteres

✓ Se comprobará que la letra este dentro del rango de letras usadas, sabiendo que
las letras usadas son: T, R, W, A, G, M, Y, F, P, D, X, B, N, J, Z, S, Q, V, H, L, C, K, E.

✓ Se comprobará que la letra corresponde al número del DNI. Sabiendo que La
letra se obtiene: calculando el resto de la división del número del DNI por 23. A
cada resultado le corresponde una letra: 0=T; 1=R; 2=W; 3=A; 4=G; 5=M; 6=Y;
7=F; 8=P; 9=D; 10=X; 11=B; 12=N; 13=J; 14=Z; 15=S; 16=Q; 17=V; 18=H; 19=L;
20=C; 21=K; 22=E.

El director del proyecto nos indica que el programa tiene que resolverse usando el
paradigma de la programación modular y nos sugiere utilizar tres funciones:
una para comprobar la cantidad de caracteres, otra para comprobar si la letra esta dentro del
rango y la ultima para comprobar si la letra se corresponde al número del DNI.
La validación será progresiva, de lo mas sencillo a lo mas complicado.

En el momento en que falle una validación se avisara al usuario que el número introducido es incorrecto.

https://en.wikipedia.org/wiki/Documento_Nacional_de_Identidad_(Spain)
http://www.interior.gob.es/web/servicios-al-ciudadano/dni/calculo-del-digito-de-control-del-nif-nie
12345678 = Z
'''

#import module for clearing the screen
import os

#About
os.system('clear')#this is only for Linux, if this code fails in Windows, put it in comment
print('-------------------------------------------------------------------------------')
print("Programa comprueba si la letra de un DNI introducido es correcta o no.")
print('-------------------------------------------------------------------------------')

#Functions
def indexNumbers(value):
    '''Function returns number from module 23 from the given value'''
    result = value % 23
    # print(f'index es {result}')
    return result

def letterDNI(index):
    '''Calcula la letra de la lista "letters", ejemplo 12345678 = Z.'''
    return letters[index]

def userInput():
    '''Input == El usuario introducirá el número de su DNI con la letra en una sola entrada'''
    print('Introduzca numero DNI para comprobar si es correcto o ficcionario.\n\
    0 para terminar el programa.')
    inputDNI = input('>')
    return inputDNI

def selectNumbers(stringOfNumbers):
    '''The function select first 8 characters from the string and change them to numbers'''
    try:
        numbers = int(stringOfNumbers[:8])     #we take out the numbers from the string
    except ValueError:
        print("Excepción ValueError")
        print("El DNI introducido ", stringOfNumbers, " no es un formato correcto.")
        numbers = -1                    #if there is error, return value that later the code will read as error
        return numbers
    else:
        return numbers

def checkLength(value):
    '''Se comprobará si el número de caracteres introducido es el correcto, sabiendo que el DNI tiene 9 caracteres'''
    if len(value) > 9:
        print('Numero introducido tiene Mas caracteres que tiene que tener.')
        return False
    elif len(value) < 9:
        print('Numero introducido tiene Menos caracteres que tiene que tener.')
        return False
    else:
        return True

def checkChar(inputDNI,letters):
    '''Funcion compruebe si la letra esta dentro del rango
    I por ejemplo no puede ser introducido'''
    character = (inputDNI[-1]).upper()
    try:
        #returns the index of the value in tuple, if there is none found, returns error
        result = letters.index(character)
    except Exception as e:
        print(f"Ha occurido error tipo: {type(e).__name__}.")
        print(f'El character final : {character}, no es un caracter valido.')
        result = False
    else:
        result = True
        return result

def main():
    '''Recursive function to check the flow of the program for errors.'''
    inputDNI = userInput()                                          #input from the user
    if inputDNI == '0':                                             #on 0 the program ends.
        print('El programa termina. Adioooos.')
    elif checkLength(inputDNI) and checkChar(inputDNI,letters):     #checks for validity of Input data-if there is an error, error will be printed out and the program will be halted-sent to main()
        numbersDNI = selectNumbers(inputDNI)                        #store the 8 numbers in variable
        # print(numbersDNI)
        # print(inputDNI)

        if numbersDNI != -1:                                        #if there was no exception
            characterDNI = indexNumbers(numbersDNI)                 #obtain index for the character list from the DNI
            resultCharacter = letterDNI(characterDNI)               #obtain letter from given DNI number
            print(f'La letra calculada de DNI introducido es:{resultCharacter}.')
            inputDNICharacter = inputDNI[-1].strip().upper()        #delete whitespace and we set it to uppercase
        else:
            main()                                                  #if there is error with input data, return to the start
        if inputDNICharacter == resultCharacter:
            print('El DNI es correcto.')
        else:
            print('El DNI NO es correcto.')
    else:                                                           #the checkLength() or checkChar() failed
        main()

#Variables
inputDNI = ''
numbersDNI = 0
letters = ('T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E')


#Program Start
main()

