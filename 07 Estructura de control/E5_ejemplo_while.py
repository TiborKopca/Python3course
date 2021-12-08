# i lleva la cuenta de números introducidos.
i = 1
# En suma se va almacenando la suma de numeros
suma = 0

#Pedimos los numeros
print("Introduce una serie de números. Si es 0 entenderemos que has terminado la lista.")
print()

# Usamos el parámetro end para que no cambie de línea. 
print("Número", i, ": ",end="")

#Pedimos el numero
numero = eval(input())

# Sacamos el número introducido por pantalla.
print('Tu numero: ',numero)

# Sumanos el primer numero a suma.
suma = suma + numero                        	

 # La condición para pedir otro número es que sea distinto de cero. 
while numero != 0:
   #incrementamos i dentro del bucle
    i = i + 1	                                 
    print("Número", i, ": ", end = "")
 
    #Pedimos el numero
    numero = eval(input())	                    
    # Sacamos el número introducido por pantalla.
    print('Tu numero: ',numero)
    #sumamos cada número a la variable suma.
    suma = suma + numero


# Al salir del while ya tendremos el valor total de la suma.
print("La suma de todos los números es:", suma)

