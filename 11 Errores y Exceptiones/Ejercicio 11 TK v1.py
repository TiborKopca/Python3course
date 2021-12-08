'''
Escribe un programa que reciba como entrada la siguiente lista
lista = [5,7,-9,'cadena']
Recorra todos los elementos de esta lista y calcule el número factorial de cada elemento (con la
función math.factorial()), mostrando el resultado por consola si no se produce ninguna
excepción.
Captura las excepciones convenientes y muestra un mensaje final, indicando el valor que se ha
procesado.
'''
#import module for clearing the screen
import os
import math

#About
os.system('clear')#this is only for Linux, if this code fails in Windows, put it in comment
print('-------------------------------------------------------------------------------')
print("Programa mostrara un error cuando hacemos operaciones matematicas con cadena de texto.")
print('-------------------------------------------------------------------------------')

lista = [5,7,-9,'cadena']
for x in lista:
    try:
        result = math.factorial(x)

    except ValueError:
        print(f"Value Error! No se puede hacer un factorial de un numero negativo:{x}.")

    except TypeError:
        print(f"Type Error! No se puede hacer un factorial de una cadena:{x}.")

    except Exception as e:
        print(f"Se ha occurido error tipo:{type(e).__name__} para valor {x}, porque es de tipo:{type(x)}.")
        print(f"Esto significa que: {e}.")

    except:
        print("Un no specificado error ha occurido.")
    else:       #no errors exists
        print(f'El factorial de {x} es {result}.')
    finally:    #executes always
        print("---------------------------------------------")

