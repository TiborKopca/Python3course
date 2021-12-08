'''Modulo que calcula la edad de la mascota y la presentación de la fecha'''
from datetime import date, datetime
#Función que calcula la edad de la mascota
def edad(myedad):
    '''Calcula la edad de la mascota'''

    #retorna el día de hoy.
    hoy = datetime.now()

    #La diferencia en años entre las dos fechas
    edad = hoy.year - myedad.year

       

    return edad

def formatoEdad(myedad):
    '''Presenta la fecha en dd de mm de yyyy'''
   
    #transformar la fechacon el formato indicado en la cadena formato.  
    fecha = myedad.strftime('%d-%m-%Y')


    return fecha

     
    
