'''Valida el sexo, la fecha de nacimiento y ele PET PASSPORT''' 
#Importamos modulos
from datetime import datetime


#Función para validar el sexo.
def sexo(mysexo):
    '''
    Función para validar el sexo.
    Guarda el sexo (solo en formato M o F).
    Utilizamos una función recursiva.
    Una función recursiva es una función que se llama a si misma.
    Si el valor introducido no es M o F se llama a ella misma hasta
    que el argumento sea el correcto.
    '''
    if (mysexo == 'M' or mysexo == 'F'):
        #Si el argumento es M o F lo devuelve para ser almacenado en la variable
        return mysexo
    else:
        #Si el argumento NO es M o F

        #solicita nuevamente el dato
        print('DATO INCORRECTO') 
        print('Sexo (M/F):')
        mysexo = input()
        #Se llama a si misma para evaluarlo (se devuelve a si misma)
        return sexo(mysexo)


#Comptueba el formato de la fecha de nacimiento
def nacimiento(fecha):
        '''Guarda la fecha de nacimiento en formato dd/mm/aaaaa'''
        try:
            #Si el formato no es el correcto se genera una excepcion
            #y la fecha no se guarda.

            #Asignamos un formato de tipo dd/mm/yyyy
            formato = '%d/%m/%Y'
            #Le asignamos el formato a fecha
            mydatetime = datetime.strptime(fecha, formato)
            
            return mydatetime
            
        except:
            #Si el formato de fecha no es dd/mm/yyyy se genera una excepcion
            #La excepcion no se captura, no hacemos nada
            
            print('DATO INCORRECTO')
            print ('Fecha de nacimiento:')
            fecha = input()
            return nacimiento(fecha)

#Comprueba el número de pasaporte
def passport(numero):
    #Obtenemos el numero de caracteres
    numCaracteres = len(numero)
    #Obtenemos las dos letras iniciales
    letras = numero[0:2]
    #Obtenemos el resto de numeros
    digitos = numero[2:11]

    #Si el numero total de caracteres es once
    #Si las dos letras iniciales son ES
    #Si los nueve digitos siguientes son numeros
    #ENTONCES y SOLO ENTONCES se asigna el numero a num_passport
        
    if ((numCaracteres == 11) and (letras == 'ES') and (digitos.isdigit())):
        return numero
    else:
        print('DATO INCORRECTO')
        print('número de PET PASSPORT')
        passport = input()
        return passport(passport)
        
            
        
        
            
            



