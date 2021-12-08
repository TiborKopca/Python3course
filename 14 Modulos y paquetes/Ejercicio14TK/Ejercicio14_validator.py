from datetime import datetime

def validateInput(value):
    '''Funcion valida el sexo, solo se admitirá M para masculino y F para femenino'''
    value = str(value)
    value = value.upper()
    # print(value)
    if(value == 'M' or value == 'F'):
       return value
    else:
        print('Solo se admitira formato M/F (macho/hembra).')
        validateInput(input('Pruebalo de nuevo:'))


#Comptueba el formato de la fecha de nacimiento
def validateBirthDates(value):
    '''Guarda la fecha de nacimiento en formato dd/mm/yyyy'''
    try:
        format = '%d/%m/%Y'                            #dd/mm/yyyy
        mydatetime = datetime.strptime(value, format)
        # print('validation of birthdate :',mydatetime)
        return mydatetime
    except Exception as e:
        #Si el formato de fecha no es dd/mm/yyyy se genera una excepcion
        # print('exception',e)
        print('Por favor, introduzca la fecha de nacimiento en formato dd/mm/yyyy:')
        return validateBirthDates(input())


def validatePassport(value):
    charactersLength = len(value)
    letters = value[0:2]
    digits = value[2:11]

    if charactersLength == 11 and letters.isalpha() and digits.isdigit():
        if letters.upper() != 'ES':
            print('Atencion! El pokemon no es de espana!')
        return value
    else:
        return validatePassport(input('Por favor, introduzca el numero de PET PASSPORT(2letras y 9digitos):'))

#tests
print(validateInput('F'))







