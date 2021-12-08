'''Importación de modulos'''

# Es posible también, importar más de un elemento en la misma
# instrucción. Para ello, cada elemento irá separado por una coma (,) y
# un espacio en blanco

# En este caso, se accederá directamente al elemento, sin recurrir a su namespace

from random import randrange, random
print("Número aleatorio(1-100): ", randrange(100))
print("Número aleatorio en coma flotante: ",random())

# No funcionara pues la función fabs no ha sido importada
print("El valor absoluto de -7 es: ", fabs(-7))

