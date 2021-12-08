#Contador

'''Se entiende por contador una variable que lleva la cuenta del número de veces que se ha cumplido una condición.
El ejemplo siguiente es un ejemplo de programa con contador (en este caso,
la variable que hace de contador es la variable cuenta)'''


'''En cada iteración, el programa comprueba si i es múltiplo de 2.
El contador se modifica sólo si la variable de control i es múltiplo de 2.
El contador va aumentando de uno en uno.
Antes del bucle se debe dar un valor inicial al contador (en este caso, 0)'''

print("Comienzo")
cuenta = 0
for i in range(1, 6):
    if i % 2 == 0:
        cuenta = cuenta + 1
print(f"Desde 1 hasta 5 hay {cuenta} múltiplos de 2")

