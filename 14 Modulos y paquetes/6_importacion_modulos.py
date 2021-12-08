'''Importación de modulos'''

# Permite importar de un módulo solo los
# elementos que se desee utilizar.

from math import pi
# from math import tau

x = pi
print('El valor de pi es: ', x)

# No funcionara, pues la función Tau no ha sido importada.
y = tau
print('El valor de Tau es: ',y)
