'''
Una función es un bloque de código con un nombre asociado,
que recibe cero o más argumentos como entrada, sigue una secuencia de sentencias,
la cuales ejecuta una operación deseada y devuelve un valor y/o realiza una tarea,
este bloque puede ser llamados cuando se necesite.

El uso de funciones es un componente muy importante del paradigma de la programación llamada estructurada,
y tiene varias ventajas:

modularización: permite segmentar un programa complejo en una serie de partes o módulos más simples,
facilitando así la programación y el depurado.
reutilización: permite reutilizar una misma función en distintos programas.
'''
#Definimos nuestra función
def hola(arg):
    """El docstring de la función"""
    print ('¡Hola', arg, '!')

#Leemos el docstring de la función
# help(hola)

#La ejecutamos
hola('Pedro') #¡Hola Pedro !
hola("Juan")
hola('Caperucita')
print()

'''
Al definir una función los valores los cuales se reciben se denominan parámetros,
pero durante la llamada los valores que se envían se denominan argumentos.
'''
#Cuando enviá argumentos a una función, estos se reciben por orden en los parámetros definidos.
#Se dice por tanto que son argumentos por posición:

#Definimos nuestra función
def resta(a, b):
    '''Resta dos numeros'''
    return a - b

#Leemos el docstring de la función
# help(resta)

#La ejecutamos y guardamos su valor de retorno en la variable resultado.
resultado = resta(30, 10)

#Presentamos por pantalla el valor de resultado
print(resultado) #20


#Sin embargo es posible evadir el orden de los parámetros
#si indica durante la llamada que valor tiene cada parámetro a partir de su nombre:
def resta(a, b):
    '''Resta dos numeros'''
    return a - b

#Leemos el docstring de la función
# help(resta)

resultado = resta(b=100, a=300)
print(resultado) #200


#Al momento de llamar una función la cual tiene definidos unos parámetros,
#si no pasa los argumentos correctamente provocará un error.
#Para evitar el error se pueden asignar parámetros por defecto.

#Si no se envia ningun argumento para los parametros a y b,
#a tomara el valor de 90 y b de 20
def resta(a = 90, b = 20):
    '''Función con parametros por defecto'''
    return a - b

#Leemos el docstring de la función
# help(resta)

#Ejecutamos la función
resultado = resta()
print(resultado)    #70
print()




#Si no se envia ningun argumento para el parametro b, tomara el valor de 30
#En este caso es necesario pasar un argumento al parametro a (le pasamos 152)
#ya que no le hemos asignado un valor por defecto

def resta(a, b = 30):
    '''Función con un parametro por defecto'''
    return a - b

#Leemos el docstring de la función
# help(resta)

#Ejecutamos la función
resultado = resta(152)
print(resultado) #122
print()





#Si se envian argumentos para los parametros a y b (en este caso 200 y 10)
# los valores por defecto (a = 90, b = 20) se ignoran

def resta(a = 90, b = 20):
    '''Función con dos parametros por defecto'''
    return a - b

#Leemos el docstring de la función
# help(resta)

#Ejecutamos la función
resultado = resta(200, 10)
print(resultado) #190
print()






#Si se envia un argumentos para el parametros b (en este caso 5)
# el valor por defecto  (b = 30) se ignora.
def resta(a, b = 30):
    '''Función con un parametro por defecto'''
    return a - b

#Leemos el docstring de la función
# help(resta)

#Ejecutamos la función
resultado = resta(65,5)
print(resultado) #60
print()





'''
En alguna ocasión no se sabe previamente cuantos argumentos necesitamos enviar a una función.
En estos casos se pueden utilizar los parámetros indeterminados por posición y por nombre.
'''

#Por posición
#Creamos una lista dinámica de argumentos por medio de una tupla.
# definiendo el parámetro con un asterisco (*args),
#para recibir los parámetros indeterminados por posición.
#Con un bucle for leemos los valores enviados a los parametros

def indeterminados_posicion(*args):
    '''Función que recibe los argumentos de una lista o tupla'''
    for arg in args:
        print (arg)
#Leemos el docstring de la función
# help(indeterminados_posicion)
#Ejecutamos la función
indeterminados_posicion("Hola",True, 1,10,20,False, "Adios")
"""
Hola
True
1
10
20
False
Adios
"""
print()

#Creamos una función que suma los argumentos que le pasamos y devuelve el valor de la suma

def sumador(*args):
    '''Función que suma los argumentos'''
    suma = 0
    for arg in args:
       suma = suma + arg
    return suma

#Leemos el docstring de la función
# help(sumador)

#Ejecutamos la función
resultado = sumador(1,1,1,1,1,10)
print(resultado)    #15
print()





#Para recibir un número indeterminado de parámetros por nombre (clave-valor)
#debemos crear un diccionario dinámico de argumentos definiendo el parámetro con dos asteriscos:

def indeterminados_nombre(**kwargs):
    '''Función que recibe los argumentos de un diccionario'''
    for kwarg in kwargs:
        print (kwarg, "=>", kwargs[kwarg])
#Leemos el docstring de la función
# help(indeterminados_nombre)

#Ejecutamos la función
indeterminados_nombre(Juan=20, Pepe=10, Antonio=80, Margarita=45)
print()
'''
Juan => 20
Pepe => 10
Antonio => 80
Margarita => 45
'''


#Los nombres args y kwargs no son obligatorios, pero se suelen utilizar por convención.
#Muchos frameworks y librerías los utilizan por lo que es una buena practica llamarlos así.

#Funciones recursivas
'''
Las funciones recursivas son funciones que se llaman a sí mismas durante su propia ejecución.
Ellas funcionan de forma similar a las iteraciones,
pero debe encargarse de planificar el momento en que dejan de llamarse a sí mismas
o tendrá una función recursiva infinita.
'''




#Calcular factorial
'''
El factorial de un número n se define como
la multiplicación de todos sus números predecesores hasta llegar a uno.
Por lo tanto 5!, leído como cinco factorial, sería 5*4*3*2*1.
'''
#Creamos la función
def factorial(n):
    '''Función que calcula el factorial'''
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

#Leemos el docstring de la función
# help(factorial)


#La ejecutamos
valor = factorial(5)
print(valor)    #120


'''
Lo que realmente hacemos con el código anterior es llamar a la función factorial() múltiples veces.
Es decir, 5! es igual a 5 * 4! y 4! es igual a 4 * 3! y así sucesivamente hasta llegar a 1.
'''

#Serie de Fibonacci

'''
Dicha serie calcula el elemento n sumando los dos anteriores n-1 + n-2.
Se asume que los dos primeros elementos son 0 y 1.
'''

#Creamos la función

def fibonacci(n):
    '''Función que calcula la serie de Fibonacci'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


'''
Siempre que la n sea distinta de cero o uno, se llamará recursivamente a la función,
buscando los dos elementos anteriores.
Cuando la n valga cero o uno se dejará de llamar a la función y se devolverá un valor concreto.
'''

#Leemos el docstring de la función
# help(fibonacci)

#Podemos calcular el elemento 7, que será 0,1,1,2,3,5,8,13, es decir, 13.

elemento = fibonacci(7)
print(elemento)     #13

