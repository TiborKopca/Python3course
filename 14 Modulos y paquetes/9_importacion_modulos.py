'''Importación de modulos'''

#También es posible importar todos los elementos
#de un módulo, sin utilizar su namespace pero tampoco alias

from math import *

print('El valor de pi es: ', pi)
print('El valor de e es: ',e)
print('El valor de τ es: ',tau)

#No funcionara. La función pertenece a otro modulo.
print('La tirada de mi dado es: ', randrange(6))

