def validarLetra(dni):
    '''Comprueba que la letra corresponde al número del DNI'''

    letras = ('T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E')

    #Calculamos la letra que nos corresponde
    caracteres = dni[0:8]
    numeros = int(caracteres)
    resto = numeros % 23
    letraLegal = letras[resto]
    #Comprobamos si tenemos la letra correcta
    #Obtenemos el ultimo caracter
    longitud = len(dni)
    letra = dni[longitud-1]
    #La comparamos con la letra que nos corresponde
    if letra == letraLegal :
        return True
    else:
        return False 
