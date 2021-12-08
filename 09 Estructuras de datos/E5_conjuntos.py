#Un conjunto se crea enmarcando sus elementos entre corchetes
conjunto1 = {1, 2, 3, 4}
print('conjunto1',conjunto1) #conjunto1 {1, 2, 3, 4}

#Sus miembros pueden ser de diversos tipos
conjunto2 = {True, 3.14, False, "Hola mundo", (1, 2)}
print('conjunto2',conjunto2) #conjunto2 {False, True, (1, 2), 3.14, 'Hola mundo'}

#Podemos obtener un conjunto a partir de una secuencia, usando la función set()
#Usando range()
conjunto3 = set(range(10))
print('conjunto3',conjunto3) #conjunto3 {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

#Desde otro conjunto
conjunto3 = set({1, 3, 4, 5, 1})
print('newSet',conjunto3)    #newSet {1, 3, 4, 5}

#Desde una lista
fromList = set([1, 3, 4, 5, 1])
print('x = ',fromList)  #x =  {1, 3, 4, 5}

#Desde una tupla
y = set((1,2,3,4,5,1))
print('Y =', y) #Y = {1, 2, 3, 4, 5}

#Desde una cadena
fromChain = set('Hola Mundo')
print('characters in set',fromChain) #characters in set {' ', 'l', 'M', 'n', 'a', 'o', 'u', 'd', 'H'}

variableText = 'Letras'
conjunto4 = set(variableText)
print('conjunto4',conjunto4) #conjunto4 {'L', 't', 'e', 'a', 'r', 's'}


#Los conjuntos son objetos mutables. Con add() y discard() podemos
#añadir y remover un elemento indicándolo como argumento
conjunto5 ={1,2,3,4,5,6}
print('conjunto5',conjunto5)    #conjunto5 {1, 2, 3, 4, 5, 6}
conjunto5.add(9)
print('conjunto5',conjunto5)    #conjunto5 {1, 2, 3, 4, 5, 6, 9}

#Eliminamos un elemento
conjunto5.discard(3)
print('conjunto5',conjunto5) #conjunto5 {1, 2, 4, 5, 6, 9}


#La función clear() elimina todos los elementos.
conjunto6 = {10,20,30,40,50,60,70,80}
print('conjunto6',conjunto6)
conjunto6.clear()
print('conjunto6',conjunto6) #conjunto6 set()


#Para saber el numero de elementos
conjunto7 = {10,2,30,4,5,60,70,80}
print('conjunto7',conjunto7)
elementos = len(conjunto7)
print('elementos del conjunto7:',elementos) #elementos del conjunto7: 8



#Para saber si un elemento es miembro del conjunto
if 2 in conjunto7:
    print('2 forma parte del conjunto')


#Para saber si un elemento NO es miembro del conjunto
if 3 not in conjunto7:
    print('3 NO forma parte del conjunto')




a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print('a = ', a)    #a =  {1, 2, 3, 4}
print('b = ', b)    #b =  {3, 4, 5, 6}
'''
La unión se realiza con el carácter | y retorna un conjunto que contiene
los elementos que se encuentran en al menos uno de los dos conjuntos
involucrados en la operación.
'''
c = a | b
print('a | b', c)   #a | b {1, 2, 3, 4, 5, 6}

'''
La intersección se realiza con el operador &, y retorna un nuevo
conjunto con los elementos que se encuentran en ambos.
'''

d = a & b
print('a & b', d)   #a & b {3, 4}

'''
La diferencia retorna un nuevo conjunto que contiene los
elementos de a que no están en b.
'''
e = a - b
print('a - b', e)   #a - b {1, 2}

#frozenset es una implementación similar a set pero inmutable

a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print('a = ', a)    #a =  frozenset({1, 2, 3})
print('b = ', b)    #b =  frozenset({3, 4, 5})
f = frozenset([3, 5, 6, 1, 5])
print('f =',f)      #f = frozenset({1, 3, 5, 6})

