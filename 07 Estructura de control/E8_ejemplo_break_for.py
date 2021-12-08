'''
La sentencia break nos permite alterar el comportamiento de los bucles
while y for. Concretamente, permite terminar con la ejecución del
bucle.
Esto significa que una vez se encuentra la palabra break, el bucle se
habrá terminado. La sentencia break rompe el flujo dentro del cuerpo
de instrucciones del bucle para abandonarlo
'''
suma = 0
for i in range(10):
    if i > 7:
        break
    suma = suma + i
print ("La suma con break ha sido: ", suma)

#----------------------------------------------------------------------------------------------
suma = 0
for i in range(10):
    suma = suma + i
print ("La suma sin break ha sido: ", suma)
