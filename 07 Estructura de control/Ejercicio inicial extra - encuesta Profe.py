'''
La empresa “El Transportes Perez SL” realizo una encuesta de satisfacción entre sus clientes y
reunió una lista de puntuaciones oscilando entre 50 y 100 puntos. Pretende clasificarlas en tres
grupos:
✓ A si la puntuación es igual o superior a 90.
✓ B si es menor que 90 pero igual o superior 75.
✓ C si es menor que 75.
Desea escribir un programa que produzca la clasificación apropiada: A,B,C y la cantidad de
encuestas que hay en cada grupo.
'''
#Declaramos las variables.
A = 0
B = 0
C = 0
puntuacion = 0

#El primer dato debe leerse antes de entrar en el bucle por primera vez,
#pues en caso contrario no se puede comprobar la condición que controla la repetición.
print('Ingrese la puntuación de la encuesta o pulse -1 para terminar')
puntuacion = float(input())

#Entramos en el bucle WHILE.
while puntuacion != -1 :
    #Entramos en una condicional multiple IF...ELIF
   # Para evitar que la marca se procese como un dato normal  puntuacion >= 0
    if puntuacion >= 0 and puntuacion < 75 :
        C = C+1
    elif puntuacion >= 75 and puntuacion < 90 :
        B = B+1

    elif puntuacion >= 90 :
        A = A+1
    #Fin del bloque IF...ELIF

    #Dentro del bucle, después de procesar el dato,
    #se debe leer un nuevo valor antes de hacer la siguiente pasada del bucle.
    print('Ingrese la puntuación de la encuesta o pulse -1 para terminar')
    puntuacion = float(input())

#Finaliza el bucle WHILE

#Presentamos los datos
print('Numero de encuestas tipo A', A)
print()
print('Numero de encuestas tipo B', B)
print()
print('Numero de encuestas tipo C', C)




