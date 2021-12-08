#Creamos la función
def calculo(num1, num2):
        '''Función que calcula La diferencia entre ellos elevada al cuadrado y luego sumado uno'''
        res = ((num1 - num2) ** 2 ) + 1
        return(res)

#Leemos el docstring de la función
print()
print(calculo.__doc__)
print()
print()


#Ejecutamos la función
numero_1 = float(input("Introcuce el primer número: "))
numero_2 = float(input("Introcuce el segundo número: "))
resultado = calculo(numero_1, numero_2)
print ("El primer número introducido ha sido: ", numero_1)
print ("El segundo número introducido ha sido: ", numero_2)
print ("La diferencia entre ellos elevada al cuadrado y luego sumado uno es: ", resultado)
print()
print()






#Creamos una función recursiva que nos pide un numero mayor que cinco
#Mientras no le demos lo que nos pide, nos lo seguira pidiendo
def numero(n):
        '''Función que nos pide un numero mayor que cinco
        y si es correcto lo guarda en la variable'''
        #Si el número es mayor que cinco devuelve el número
        if n > 5:
                return n
        else:
                #Si el numero es inferior a cinco
                #Solicita nuevamente el dato
                print('Introduzca un número superior a cinco')
                num = float(input())
                 #Se llama a si misma para evaluarlo (se devuelve a si misma)
                return numero(num)

#Leemos el docstring de la función
print()
print()
print(numero.__doc__)
print()
print()

#Ejecutamos la función
print('Introduzca un número superior a cinco')
num = float(input())

valor = numero(num)

print ("El número introducido ha sido: ", valor)
print()
print()

#Creamos una función que toma los datos de una tupla y devuelve la media de los datos
def media(*args):
        '''Función que toma los datos de una tupla
        y devuelve la media de los mismos'''
        suma = 0
        numeros = 0
        media = 0
        for a in args:
                suma = suma + a
                numeros = numeros + 1
        media = suma/numeros
        return media

#Leemos el docstring de la función
print()
print()
print(media.__doc__)
print()
print()



#Ejecutamos la función

#Creamos la tupla
notas = (5,5,5,5,5)

#Ejecutamos la función
mymedia = media(*notas)#No olvidar el asterisco *
print('La media obtenida es: ', mymedia)



