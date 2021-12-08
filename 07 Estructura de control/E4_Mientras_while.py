#Repetitiva Mientras (while)

# El siguiente programa escribe los números del 1 al 3:
i = 1
while i <= 3:
    print(i)
    i += 1
print("Programa terminado")

#-----------------------------------------------------------------------------------------------------

# El siguiente ejemplo pide un número positivo
# al usuario una y otra vez hasta que el usuario lo haga correctamente.

#Pide el dato antes de entrar en el bucle
numero = int(input("Escriba un número positivo: "))

#Si el numero es menor que cero (negativo) entra en el bucle
while numero < 0:
    #Informa del error y vuelve a pedir el numero
    print("¡Ha escrito un número negativo!",numero, "Inténtelo de nuevo")
    numero = int(input("Escriba un número positivo: "))

#Cuando escriba el dato correcto se ejecuta
print("Ha escrito",numero)
print("Gracias por su colaboración")

