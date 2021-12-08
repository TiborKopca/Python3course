#Selectiva simple (Condicional simple)

'''La estructura de control if ...
permite que un programa ejecute unas instrucciones
cuando se cumplan una condición. '''

'''La primera línea contiene la condición a evaluar y es una expresión lógica.
Esta línea debe terminar siempre por dos puntos (:).'''

'''La condición se evalúa siempre.
Si el resultado es True se ejecuta el bloque de sentencias
Si el resultado es False no se ejecuta el bloque de sentencias.'''

'''A continuación viene el bloque de órdenes que se ejecutan cuando la condición se cumple
(es decir, cuando la condición es verdadera).
Es importante señalar que este bloque debe ir sangrado, puesto que Python utiliza el sangrado
para reconocer las líneas que forman un bloque de instrucciones.
El sangrado que se suele utilizar en Python es de cuatro espacios,
pero se pueden utilizar más o menos espacios.
Al escribir dos puntos (:) al final de una línea,
el editor sangrará automáticamente las líneas siguientes.
Para terminar un bloque, basta con volver al principio de la línea.'''

'''El programa siguiente pide un número positivos al usuario y almacena la respuesta en la variable "numero".
Después comprueba si el número es negativo.
Si lo es, el programa avisa que no era eso lo que se había pedido.
Finalmente, el programa imprime siempre el valor introducido por el usuario. '''


numero = int(input("Escriba un número positivo: "))
if numero < 0:
    print("¡Le he dicho que escriba un número positivo!")
print(f"Ha escrito el número {numero}")


