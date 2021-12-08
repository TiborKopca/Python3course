'''Este es el módulo principal (archivo de nivel superior) desde el cual se inicia la aplicación'''
#Importamos un módulo definido por el usuario
import myModulo

#Importamos un módulo de la biblioteca standar
import random

#Esta es la función principal
#desde ella se inicia la aplicación
def main():
    print("Este es el módulo principal que ira llamando a los otros módulos")
    print('Obtenemos la información del módulo definido por el usuario myModulo con la función help()' )
    print('----------------------------------------------------------------------------------------')

    #función help()
    help(myModulo)
    print('----------------------------------------------------------------------------------------')

    print('Obtenemos la información de la funciónSuma() \n dentro del módulo definido por el usuario myModulo \n con la función help()' )
    #función help() para obtener información de la funciónSuma
    help(myModulo.funcionSuma)
    print('----------------------------------------------------------------------------------------')

    print('Vemos cuales son los componentes del módulo con la función dir()')
    #Función dir()
    print(dir(myModulo)) #['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'funcionSuma', 'primeraFuncion', 'segundaFuncion']
    print('----------------------------------------------------------------------------------------')



    #Ejecutamos la primeraFuncion() del módulo definido por el usuario myModulo
    myModulo.primeraFuncion()           #Esta es la primera función
    print('----------------------------------------------------------------------------------------')
    #Ejecutamos la funcion randrange() de la libreria estandar random
    resultado = random.randrange(6)
    print('Mi número ha sido de: ', resultado) #will print the number from range 0-6
    print('----------------------------------------------------------------------------------------')

    #Ejecutamos la funcionSuma() del módulo definido por el usuario myModulo
    n1 = float(input('Escriba el primer número: '))
    n2 = float(input('Escriba el segundo número: '))
    resultado = myModulo.funcionSuma(n1,n2)
    print('La suma de', n1, 'con', n2, 'da el resultado de', resultado)
    print('----------------------------------------------------------------------------------------')



if __name__ == '__main__':
    main()






