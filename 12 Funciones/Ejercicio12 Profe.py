def caracteres(DNI):

    '''Comprueba el numero de caracteres y devuelve true o false'''
    #Obtenemos el numero de caracteres
    numCaracteres = len(DNI)
    #Hacemos la comprobacion
    if numCaracteres == 9 :
        return True
    else:
        return False


def letra(DNI, letras):
    '''Comprueba que la letra este dentro del rango de letras usadas por el DNI'''
    #Obtenemos el ultimo caracter
    longitud = len(DNI)
    letra = DNI[longitud-1]
    #Comprobamos si es una letra
    esLetra = letra.isalpha()

    #Si es una letra se comprueba si esta en la tupla
    if esLetra :
        if letra in letras:
            return True
        else:
            return False
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





letras = ('T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E')

#Pedimos el numero de DNI
print('Introduzca su numero de DNI:')
mydni = input()

#Eliminamos los espacios que el usuario introduzca junto con el número del DNI.
mydni = mydni.replace('  ','')

#Eliminamos los puntos que el usuario introduzca junto con el número del DNI.
mydni = mydni.replace('.','')

#Eliminamos los guiones que el usuario introduzca junto con el número del DNI.
mydni = mydni.replace('-','')

#Eliminamos los guiones bajos que el usuario introduzca junto con el número del DNI.
mydni = mydni.replace('_','')

#Lo ponemos todo em mayusculas
mydni = mydni.upper()

#Comprobamos el numero de caracteres
if caracteres(mydni):
    #Comprobamos si la letra este dentro del rango de letras usadas por el DNI
    if letra(mydni, letras):
        #Comprobamos si la letra es correcta
        if validar(mydni, letras):
            print('Su DNI es correcto')
        else:
            print('La letra de su DNI no es la que le corresponde')
    else:
        print('La letra introducida no es ninguna de las usadas en los DNI')
else:
    print('El numero de caracteres introducido no es correcto')
