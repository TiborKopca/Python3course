#Selectiva doble

'''La estructura de control if ... else ...
permite que un programa ejecute unas instrucciones cuando se cumple una condición
y otras instrucciones cuando no se cumple esa condición. '''

'''La primera línea contiene la condición a evaluar. Esta línea debe terminar siempre por dos puntos (:).'''

'''La condición se evalúa siempre.
Si el resultado es True se ejecuta solamente el bloque de sentencias 1
Si el resultado es False se ejecuta solamente el bloque de sentencias 2.'''

'''A continuación viene el bloque de órdenes que se ejecutan cuando la condición se cumple (es decir, cuando la condición es verdadera). '''

'''Después viene la línea con la orden else,
que indica a Python que el bloque que viene a continuación se tiene que ejecutar
cuando la condición no se cumpla (es decir, cuando sea falsa).
Esta línea también debe terminar siempre por dos puntos (:).
La línea con la orden else no debe incluir nada más que el else y los dos puntos.
En último lugar está el bloque de instrucciones sangrado que corresponde al else.'''

''' El programa siguiente pregunta la edad al usuario y almacena la respuesta en la variable "edad".
Después comprueba si la edad es inferior a 18 años.
Si esta comparación es cierta, el programa escribe que es menor de edad y si es falsa escribe que es mayor de edad.
Finalmente el programa siempre se despide, ya que la última instrucción está fuera de cualquier bloque y por tanto se ejecuta siempre. '''
print('----------------------------------------')

edad = int(input("¿Cuántos años tiene? "))
if edad < 18:
    print("Es usted menor de edad")
else:
    print("Es usted mayor de edad")
print("¡Hasta la próxima!")


'''Un bloque de instrucciones puede contener varias instrucciones.
Todas las instrucciones del bloque deben tener el mismo sangrado'''

print('-------------------------------------------------')

edad = int(input("¿Cuántos años tiene? "))
if edad < 18:
    print("Es usted menor de edad")
    print("Recuerde que está en la edad de aprender")
else:
    print("Es usted mayor de edad")
    print("Recuerde que debe seguir aprendiendo")
print("¡Hasta la próxima!")
