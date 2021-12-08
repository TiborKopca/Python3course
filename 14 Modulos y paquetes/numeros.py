'''Módulos definidos por el usuario'''

#Función que suma una secuencia de numeros
def sumasecuencia(numero):
    '''Suma todos los números consecutivos desde 1 hastael número expresado.
    Si el valor es menor que 1 devuelve 0'''

    ntotal= 0
    if numero >0:
        mylista = list(range(1,numero+1))
        for nnum in mylista:
            ntotal = ntotal + nnum
    return ntotal


#Función que multiplica dos numeros
def multiply(a,b):
    '''Multiplica dos números'''
    resultado = float(a) * float(b)
    return resultado


 
#Función que obtiene el cuadrado de un número
def cuadrado(n):
    '''obtiene el cuadrado de un número'''
    resultado = n**2
    return resultado

#Función que obtiene el cubo de un numero
def cubo(n):
    '''obtiene el cubo de un numero'''
    resultado = n**3
    return resultado


