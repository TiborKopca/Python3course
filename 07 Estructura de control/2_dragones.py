import random
import time

# Introducción
print('Estás en una tierra llena de dragones. Frente a tí')
print('hay dos cuevas. En una de ellas, el dragón es generoso y')
print('amigable y compartirá su tesoro contigo. El otro dragón')
print('es codicioso y está hambriento, y te devorará inmediatamente.')
print()

# ElegirCueva
# La primera vez que se comprueba la condición de la sentencia while, cuevaElegida está definida como
# la cadena vacía, ''. La cadena vacía no es igual a la cadena '1', luego el lado izquierdo se evalúa
# a True. La cadena vacía tampoco es igual a la cadena '2', por lo que el lado derecho se evalúa a True.
# Entonces la condición se transforma en True and True. Como ambos valores Booleanos son
# True, la condición finalmente se evalúa a True. Luego la ejecución del programa entra al bloque while.

# Si el jugador ha ingresado 1 ó 2, entonces cueva será '1' or '2' (ya que input() siempre
# devuelve cadenas). Esto hace que la condición sea False, y la ejecución del programa continuará
# debajo del bucle while.
# Pero si el jugador hubiese escrito 3 o 4 o HOLA, esa respuesta habría sido inválida. La condición
# seguiría siendo True y entrando al bloque while para preguntar de nuevo al jugador. El programa
# simplemente continúa preguntando hasta que el jugador responda 1 or 2. Esto garantiza que
# cuando la ejecución continúe avanzando la variable cueva contendrá una respuesta válida.

cuevaElegida = ''

#INICIO BUCLE
while cuevaElegida != '1' and cuevaElegida != '2':
   print('¿A qué cueva quieres entrar? (1 ó 2)')
   cuevaElegida = input()
#FIN BUCLE

# Explorar la Cueva
# La función random.randint() que devolverá 1 ó 2. Este valor entero se
# almacena en cuevaAmigable y representa la cueva con el dragón amigable

cuevaAmigable = random.randint(1, 2)


print('Te aproximas a la cueva...')

time.sleep(2)

print('Es oscura y espeluznante...')

time.sleep(2)

print('¡Un gran dragon aparece súbitamente frente a tí! Abre sus fauces y ...')

time.sleep(2)

# El valor en cuevaAmigable es un entero porque random.randint() devuelve enteros. No
# puedes comparar cadenas y enteros con el signo ==, porque siempre resultarán distintas. '1' no
# es igual a 1 y '2' no es igual a 2.
# Entonces se pasa cuevaAmigable a la función str(), la cual devuelve el valor de cadena de
# cuevaAmigable. De esta manera los valores serán el mismo tipo de datos y pueden ser comparados

if cuevaElegida == str(cuevaAmigable):
   print('¡Te regala su tesoro!')
else:
   print('¡Te engulle de un bocado!') 
