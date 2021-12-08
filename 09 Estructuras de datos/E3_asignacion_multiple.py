#Asignación múltiple
#En una sola instrucción, estamos declarando tres variables: a, b, c y
#asignándoles un valor concreto a cada una.

a, b, c = 'string', 15, True
print("Valor de a: ", a)
print("Valor de b: ", b)
print("Valor de c: ", c)

print('-----------------------------------------------')

#La asignación múltiple de variables, también puede darse utilizando
#como valores, el contenido de una tupla o también, de una lista
#Esto se llama desenpaquetado de secuencias.

mi_tupla = ('hola mundo', 2021)
texto, anio = mi_tupla
print("Valor de texto: ", texto)    #hola mundo
print("Valor de anio: ", anio)      #2021

print('-----------------------------------------------')

mi_lista = ['España', 'Baleares']
pais, provincia = mi_lista
print("Valor de pais: ", pais)              #España
print("Valor de provincia: ", provincia)    #Baleares

print('-----------------------------------------------')

'''
Si a una variable se le asigna una secuencia de valores separados por comas, el valor de esa variable será la tupla formada por todos los valores asignados. A esta operación se la denomina empaquetado de
secuencias.
'''
#Se crea la tupla
myTupla = 'Pedro', 25, 48.14, 'Juan'
for i in myTupla:
    print(i) #print value in each row
