def esLetra(dni):
    '''Comprueba si el ultimo caracter es una letra y esta dentro del rango'''

    letras = ('T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E')

    #Obtenemos el ultimo caracter
    longitud = len(dni)
    letra = dni[longitud-1]
    #Comprobamos si es una letra
    esLetra = letra.isalpha()

    if esLetra:
        if letra in letras:
                return True
        else:
                return False 
        
       
    else:
        return False
    
