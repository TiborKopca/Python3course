def checkLength(value):
    '''Se comprobará si el número de caracteres introducido es el correcto, sabiendo que el DNI tiene 9 caracteres'''
    characterCount = len(value)
    if characterCount > 9:
        print('Numero introducido tiene MAS caracteres que tiene que tener.')
        return False
    elif characterCount < 9:
        print('Numero introducido tiene MENOS caracteres que tiene que tener.')
        return False
    else:
        return True
