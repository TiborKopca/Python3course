'''
La sentencia break nos permite alterar el comportamiento de los bucles
while y for. Concretamente, permite terminar con la ejecución del
bucle.
Esto significa que una vez se encuentra la palabra break, el bucle se
habrá terminado. La sentencia break rompe el flujo dentro del cuerpo
de instrucciones del bucle para abandonarlo
'''
suma = 0
print("El programa irá pidiendo números y los irá sumando hasta que la suma supere el valor 100")
while True:
    numero = eval(input("Introduce un número: "))
    suma = suma + numero
    if suma > 100:
        break
print ("La suma total al superar los 100 ha sido: ", suma)
