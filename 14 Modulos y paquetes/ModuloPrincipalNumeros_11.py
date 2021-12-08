'''el Modulo Principal de numeros_11'''
import numeros as n

#Esto hace que sea el modulo principal
if __name__ == "__main__":

    #Pedimos los datos
    print('Cual es el ultimo número de la secuenca que quiere sumar:')
    numero1 = int(input())
    print()
    print()
    print('Inserte el primer número para multiplicar:')
    numero2 = float(input())
    print()
    print()
    print('Inserte el segundo número para multiplicar:')
    numero3 = float(input())
    print()
    print()
    print('Inserte un número para elevar al cuadrado')
    numero4 = float(input())
    print()
    print()
    print('Inserte un número para elevar al cubo')
    numero5 = float(input())
    print()
    print()

    #Ejecutamos las funciones
    suma = n.sumasecuencia(numero1)
    multiplica = n.multiply(numero2,numero3)
    cuadrado = n.cuadrado(numero4)
    cubo = n.cubo(numero5)

    #Mostramos los resultados
    print('La suma de la secuencia del 1 al',numero1, 'da el resultado de:',suma)
    print()
    print('La multiplicación de', numero2, 'por', numero3, 'da el resultado de:', multiplica)
    print()
    print('El cuadrado de',numero4, 'es',cuadrado)
    print()
    print('El cubo de', numero5, 'es', cubo)
    print()
    
 

    
