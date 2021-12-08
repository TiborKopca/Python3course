'''statistics: módulo que permite utilizar funciones estadísticas básicas.'''

'''
El módulo statistics te va a permitir realizar cálculos estadísticos sobre
conjuntos de datos.

'''

import statistics
import random
valores = random.sample(range(10), 8)
print("Número aleatorios generados: ", valores)         #Número aleatorios generados:  [8, 4, 3, 1, 0, 6, 2, 9]
print("Media: ", statistics.mean(valores))                      #Media:  4.125
print("Mediana: ", statistics.median(valores))                  #Mediana:  3.5
print("Mediana inferior: ", statistics.median_low(valores))     #Mediana inferior:  3
print("Mediana superior: ", statistics.median_high(valores))    #Mediana superior:  4
print("Varianza: ", statistics.variance(valores))               #Varianza:  10.696428571428571






