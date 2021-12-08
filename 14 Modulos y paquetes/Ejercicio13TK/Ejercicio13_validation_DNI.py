def letterIndexCalculation(numericalValue):
    '''Function returns number from module 23 from the given value'''
    index = numericalValue % 23
    # print(f'index es {result}')
    return index

def letterDNICalculated(index,list):
    '''Calcula la letra de la lista dada, por ejemplo en "letters", index 14 es letra Z.'''
    letterCalculatedFromList = list[index]
    return letterCalculatedFromList

def validate(character1,character2):
    '''Comprueba que la letra corresponde al numero del DNI, ejemplo 12345678 = Z'''
    if character1 == character2:
        return True
    else:
        return False


def validar(DNI, letras):
    '''Comprueba que la letra corresponde al número del DNI'''
    #Calculamos la letra que nos corresponde
    caracteres = DNI[0:8]
    numeros = int(caracteres)
    resto = numeros % 23
    letraLegal = letras[resto]

    #Comprobamos si tenemos la letra correcta
    #Obtenemos el ultimo caracter
    longitud = len(DNI)
    letra = DNI[longitud-1]
    #La comparamos con la letra que nos corresponde
    if letra == letraLegal :
        return True
    else:
        return False