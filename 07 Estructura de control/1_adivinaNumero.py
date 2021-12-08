# Este es el juego de adivinar el número.

#  importa el módulo llamado random de modo que el programa pueda llamar a
#  random.randint(). Esta función generará un número aleatorio para que el usuario adivine.

import random

# Guardaremos en esta variable
# el número de veces que el jugador ha intentado adivinar el número

intentosRealizados = 0

print('¡Hola! ¿Cómo te llamas?')
miNombre = input()

# La función randint() devolverá un entero aleatorio en el intervalo comprendido (incluidos los
# bordes) entre los dos argumentos enteros que le pases.
# El entero aleatorio devuelto por randint() es almacenado en una variable llamada número;
# este es el número secreto que el jugador intentará adivinar. 

numero = random.randint(1, 20)
print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 20.')

# Varias líneas de código pueden ser agrupadas en un bloque. Un bloque consiste en líneas de
# código que comparten mínima indentación posible. Puedes ver dónde comienza y termina un
# bloque de código mirando el número de espacios antes de las líneas. Esto se llama la indentación de la línea.

# Un bloque comienza cuando la indentación de una línea se incrementa (usualmente en cuatro
# espacios). Cualquier línea subsiguiente que también esté indentada por cuatro espacios es parte
# del bloque. El bloque termina cuando hay una línea de código con la misma indentación que antes
# de empezar el bloque. Esto significa que pueden existir bloques dentro de otros bloques.

# La sentencia while (mientras) indica el comienzo de un bucle. Los bucles pueden ejecutar el
# mismo código repetidas veces. Cuando la ejecución llega hasta una sentencia while, evalúa la
# condición junto a la palabra reservada while. Si la condición se evalúa a True, la ejecución se
# mueve dentro del bloque while. 
#Si la condición se evalúa a False, la ejecución se mueve hasta debajo del bloque while

# Una sentencia while siempre incluye dos punos (el signo :) después de la condición.

# INICIO WHILE
while intentosRealizados < 6:
    print('Intenta adivinar.') # Hay cuatro espacios delante de print.
    estimación = input()
    estimación = int(estimación)
   
    intentosRealizados = intentosRealizados + 1

    if estimación < numero:
       print('Tu estimación es muy baja.') # Hay ocho espacios.

    if estimación > numero:
       print('Tu estimación es muy alta.')

    if estimación == numero:
       break
# FIN WHILE

# Una sentencia break indica a la ejecución que salga inmediatamente del bucle while y se mueva
# a la primera línea a continuación del mismo. 

if estimación == numero:
        intentosRealizados = str(intentosRealizados)
        print('¡Buen trabajo, ' + miNombre + '! ¡Has adivinado mi número en ' +intentosRealizados + ' intentos!')

if estimación != numero:
        numero = str(numero)
        print('Pues no. El número que estaba pensando era ' + numero)
   

   
      
 
 
