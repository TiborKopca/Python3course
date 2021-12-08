#Acumulador

'''Se entiende por acumulador una variable que acumula el resultado de una operación.
El ejemplo siguiente es un ejemplo de programa con acumulador
(en este caso, la variable que hace de acumulador es la variable suma)'''

'''El acumulador se modifica en cada iteración del bucle
(en este caso, el valor de i se añade al acumulador suma).
Antes del bucle se debe dar un valor inicial al acumulador (en este caso, 0)'''


print("Comienzo")
suma = 0
for i in [1, 2, 3, 4]:
    suma = suma + i
print(f"La suma de los números de 1 a 4 es {suma}")
