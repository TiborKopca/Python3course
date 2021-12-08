''' Escribe un programa que reciba como entrada la siguiente lista
lista = [5,7,-9,'cadena']
Recorra todos los elementos de esta lista y calcule el número factorial de cada elemento
(con la función math.factorial()), mostrando el resultado por consola si no se
produce ninguna excepción. Captura las excepciones convenientes y muestra un
mensaje final, indicando el valor que se ha procesado. '''

#Importamos el modulo math para el calculo del factorial
import math

#Creamos la lista
lista = [5,7,-9,'cadena']

#Recorremos la lista y calculamos el factorial
for valor in lista:
    try:
        factorial = math.factorial(valor)

    except TypeError:
        print("Excepción TypeError:")
        print("No se puede calcular el factorial para el tipo de dato: ", type(valor))


    except ValueError:
        print("Excepción ValueError")
        print("El valor ", valor, " no es un entero positivo")

    else:
        #Se ejecuta si no se produce ninguna excepción
        print("El factorial de ", valor, " es ", factorial)

    finally:
        #Se ejecuta siempre
        print("El valor procesado es: ", valor)
