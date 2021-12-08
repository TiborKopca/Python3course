def checkLastCharacter(inputDNI,letters):
    '''Funcion compruebe si la letra esta dentro del rango. I por ejemplo no puede ser introducido.'''
    print(inputDNI)
    character = (inputDNI[-1])              #obrain the value of the last character

    if character.isalpha():                 #check if the last character is letter, not number
        pass
    else:
        print(f'El character final : {character}, no es un caracter valido, porque no es una Letra.')
        return False

    try:
        #returns the index of the value in tuple, if there is none found, returns error
        result = letters.index(character)
    except Exception as e:
        print(f"Ha occurido error tipo: {type(e).__name__}.")
        print(f'El character final : {character}, no es un caracter valido, no existe esta combinacion.')
        result = False
    else:
        result = True
        return result


# def letra(DNI, letras):
#     '''Comprueba que la letra este dentro del rango de letras usadas por el DNI'''
#     #Obtenemos el ultimo caracter
#     longitud = len(DNI)
#     letra = DNI[longitud-1]
#     #Comprobamos si es una letra
#     esLetra = letra.isalpha()

#     #Si es una letra se comprueba si esta en la tupla
#     if esLetra :
#         if letra in letras:
#             return True
#         else:
#             return False
#     else:
#         return False
