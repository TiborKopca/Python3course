#Author : Tibor Kopca
#Curso : Introducció a la programació estructurada i modular amb python
#Fecha : 03/12/2021
'''
Escriba una función que calcule la letra del DNI a partir del número.
 La letra se obtiene calculando el resto de la división del número del DNI por 23. A cada resultado
le corresponde una letra: 0=T; 1=R; 2=W; 3=A; 4=G; 5=M; 6=Y; 7=F; 8=P; 9=D; 10=X; 11=B; 12=N;
13=J; 14=Z; 15=S; 16=Q; 17=V; 18=H; 19=L; 20=C; 21=K; 22=E.
Después de obtener la letra preguntar si desea realizar otro calculo. Ejecutar nuevamente la
función hasta que no desee hacer más cálculos
'''
#import module for clearing the screen
import os
import time

#About
# os.system('clear')#this is only for Linux, if this code fails in Windows, put it in comment
print('-------------------------------------------------------------------------------')
print("Programa calcule la letra del DNI a partir del número.")
print('-------------------------------------------------------------------------------')

#Constants
LETTERS = ('T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E')

def prepareData(value):
    '''Borra los datos no deseados.'''
    value = str(value).replace(" ", "").replace('-','').replace('_','').replace('.','').strip()
    return value

def checkLength(value):
    '''Se comprobará si el número de caracteres introducido tiene solo 8 caracterers'''
    if len(value) > 8:
        print('Numero introducido tiene Mas caracteres que tiene que tener(8).')
        return False
    elif len(value) < 8:
        print('Numero introducido tiene Menos caracteres que tiene que tener(8).')
        return False
    else:
        return True

def calcularDNI(value):
    '''Devuelve la letra de la tupla con el parametro como el index de la tupla.'''
    value = int(value)
    module = value % 23
    letter = LETTERS[module]
    return letter

def newCalculationValidation(value):
    '''Validara si el argumento vale string == "SI" '''
    if value == 'si' or value == 'SI':
        return True
    else:
        return False

def numberValidation(value):
    '''Validara si el argumento es numero. Devuelve True en caso si, False en caso no.'''
    if value.isdigit():
        return True
    else:
        return False

def questionAgain():
    print('Si quiere probarlo de nuevo, escribe "si".')
    if newCalculationValidation(input()):
        main()
    else:
        print('El programa se acaba. Adios.')

def main():
    '''Handles program flow'''
    inputData = input('Introduzca el numero para calcular la letra que pertenece a numero :')
    inputData = prepareData(inputData)

    if checkLength(inputData) and numberValidation(inputData):

        resultLetter = calcularDNI(inputData)
        print('calculando...')
        time.sleep(2)
        print('calculando...')
        time.sleep(3)
        print('calculando...')
        time.sleep(1)
        print("-----------------------------------------------------------------")
        print(f'La letra corespondiente al numero {inputData} es {resultLetter}.')
        questionAgain()
    else:
        print('La validacion ha fallado. Los datos introducidos no es numero.')
        questionAgain()


#Program Start
if __name__ == '__main__':
    main()

