#Las listas en Python son una secuencia de valores los cuales pueden ser de cualquier tipo,
#cadenas, números, floats, contenido mixto o lo que sea.

mylist0 = [1, 2, 3, 4, 5]
mylist1 = ['one', 'two', 'three', 'four', 'five']
mylist2 = ['one', 20 , 5.5 , [10, 15], 'five']
print(mylist0) #[1, 2, 3, 4, 5]
print(mylist1) #['one', 'two', 'three', 'four', 'five']
print(mylist2) #['one', 20, 5.5, [10, 15], 'five']

print('-----------------------------------------------------')

#Podemos generar una lista con valores enteros con la función range()
mi_lista = list(range(7))
print(mi_lista) #[0, 1, 2, 3, 4, 5, 6]

print('-----------------------------------------------------')

#Los elementos se pueden cambiar o reordenar.
#Podemos cambiar el tercer elemento de la siguiente forma:
print('ejemplo 1')
mylist = ['one', 'two', 'three', 'four', 'five']
print(mylist) #['one', 'two', 'three', 'four', 'five']
mylist[2] = "New item"
print(mylist) #['one', 'two', 'New item', 'four', 'five']

print('-----------------------------------------------------')

#Si el índice es negativo, cuenta desde el último elemento.
print('ejemplo 2')
mylist = ['one', 'two', 'three', 'four', 'five']
elem = mylist[-1]
print(elem) #five

print('-----------------------------------------------------')
#Puedes leer los elementos de la lista
#utilizando un ciclo for de la siguiente forma:
print('ejemplo 3')
mylist = ['one', 'two', 'three', 'four', 'five']
for elem in mylist:
    print(elem) #will print in rows all data in 'mylist'

print('-----------------------------------------------------')

#La función len ( ) se utiliza para devolver la cantidad de elementos,
#mientras que la función range () devuelve la lista de índices.
#Puedes realizar operaciones:
print('ejemplo 4')
mylist = [1, 2, 3, 4, 5]
print(mylist) #[1, 2, 3, 4, 5]
for i in range(len(mylist)):
    mylist[i]+=5
print(mylist) #[6, 7, 8, 9, 10]

print('-----------------------------------------------------')

#Puede cortar una lista usando el operador (:) de esta manera:
print('ejemplo 5')
mylist = ['one', 'two', 'three', 'four', 'five']
print(mylist)       #['one', 'two', 'three', 'four', 'five']
print(mylist[1:3])  #['two', 'three']
print(mylist[1:3])  #['two', 'three']
print(mylist[1:])   #['two', 'three', 'four', 'five']
print(mylist[:3])   #['one', 'two', 'three']
print(mylist[:])    #['one', 'two', 'three', 'four', 'five']

print('-----------------------------------------------------')

#Puedes cambiar los elementos utilizando el operador de corte:
print('ejemplo 6')
mylist = ['one', 'two', 'three', 'four', 'five']
mylist[1:3] = ['Hello', 'Guys']
print(mylist)   #['one', 'Hello', 'Guys', 'four', 'five']

print('-----------------------------------------------------')

#Puede usar el método insert para insertar un elemento en la lista
print('ejemplo 7')
mylist = [1, 2, 3, 4, 5]
print(mylist)               #[1, 2, 3, 4, 5]
mylist.insert(1,'Hello')
print(mylist)               #[1, 'Hello', 2, 3, 4, 5]

print('-----------------------------------------------------')

#Para agregar un elemento a una lista, puedes utilizar el método de agregar:
print('ejemplo 8')
mylist = ['one', 'two', 'three', 'four', 'five']
print(mylist)           #['one', 'two', 'three', 'four', 'five']
mylist.append("new one")
print(mylist)           #['one', 'two', 'three', 'four', 'five', 'new one']

print('-----------------------------------------------------')

#Puede agregar más de un elemento usando el método extend:
print('ejemplo 9')
mylist = ['one', 'two', 'three', 'four', 'five']
print(mylist)               #['one', 'two', 'three', 'four', 'five']
list2 = ["Hello", "Guys"]
print(list2)                #['Hello', 'Guys']
mylist.extend(list2)
print(mylist)               #['one', 'two', 'three', 'four', 'five', 'Hello', 'Guys'

print('-----------------------------------------------------')

#Para ordenar una lista, utiliza el método sort.
print('ejemplo 10')
mylist = ['cde', 'fgh', 'abc', 'klm', 'opq']
print(mylist)           #['cde', 'fgh', 'abc', 'klm', 'opq']
mylist.sort()
print(mylist)           #['abc', 'cde', 'fgh', 'klm', 'opq']

list2 = [3, 5, 2, 4, 1]
print(list2)            #[3, 5, 2, 4, 1]
list2.sort()
print(list2)            #[1, 2, 3, 4, 5]

print('-----------------------------------------------------')

#Puedes invertir el orden de una lista en Python usando el método reverse
print('ejemplo 11')
mylist = [1, 2, 3, 4, 5]
print(mylist)           #[1, 2, 3, 4, 5]
mylist.reverse()
print(mylist)           #[5, 4, 3, 2, 1]

print('-----------------------------------------------------')

#Puede usar el método index para obtener el índice de un elemento
print('ejemplo 12')
mylist = ['one', 'two', 'three', 'four', 'five']
print(mylist)                   #['one', 'two', 'three', 'four', 'five']
print(mylist.index('two'))      #1

print('-----------------------------------------------------')

#Puedes eliminar un elemento especificando el índice del elemento al método pop
print('ejemplo 13')
mylist = ['one', 'two', 'three', 'four', 'five']
removed = mylist.pop(2)
print(mylist)           #['one', 'two', 'four', 'five']
print(removed)          #three

print('-----------------------------------------------------')

#Si no especificas un índice para el método pop, eliminará el último elemento.
print('ejemplo 14')
mylist = ['one', 'two', 'three', 'four', 'five']
removed = mylist.pop()
print(mylist)           #['one', 'two', 'three', 'four']
print(removed)          #five

print('-----------------------------------------------------')

#También puedes eliminar un elemento utilizando el método remove
print('ejemplo 15')
mylist = ['one', 'two', 'three', 'four', 'five']
print(mylist)           #['one', 'two', 'three', 'four', 'five']
mylist.remove('two')
print(mylist)           #['one', 'three', 'four', 'five']

print('-----------------------------------------------------')

#Puedes utilizar el operador del para eliminar un elemento:
print('ejemplo 16')
mylist = ['one', 'two', 'three', 'four', 'five']
print(mylist)           #['one', 'two', 'three', 'four', 'five']
del mylist[2]
print(mylist)           #['one', 'two', 'four', 'five']

print('-----------------------------------------------------')

#Puedes eliminar múltiples elementos usando un operador de corte.
print('ejemplo 17')
mylist = ['one', 'two', 'three', 'four', 'five']
print(mylist)           #['one', 'two', 'three', 'four', 'five']
del mylist[1:3]
print(mylist)           #['one', 'four', 'five']

print('-----------------------------------------------------')

#Puedes utilizar el signo más (+) para combinar listas de la siguiente forma:
print('ejemplo 18')
list1 = [1, 2, 3]
print(list1)            #[1, 2, 3]
list2 = [4, 5, 6]
print(list2)            #[4, 5, 6]
print(list1 + list2)    #[1, 2, 3, 4, 5, 6]

print('-----------------------------------------------------')

#Además, puedes repetir una lista usando
#el operador de multiplicar de esta manera:
print('ejemplo 19')
list1 = [1, 2, 3]
print(list1)
print(list1 * 2)    #[1, 2, 3, 1, 2, 3]

print('-----------------------------------------------------')

#Para convertir una cadena en caracteres separados, puede usar la función list
print('ejemplo 20')
mystr = "LikeGeeks"
print(mystr)     #LikeGeeks
mylist = list(mystr)
print(mylist)    #['L', 'i', 'k', 'e', 'G', 'e', 'e', 'k', 's']

print('-----------------------------------------------------')

#Puedes usar el método split para dividir el texto en palabras:
print('ejemplo 21')
mystr = "Welcome to likegeeks website"
print(mystr)        #Welcome to likegeeks website
mylist = mystr.split()
print(mylist)       #['Welcome', 'to', 'likegeeks', 'website']

mystr = "Welcome-to-likegeeks-website"
print(mystr)        #Welcome-to-likegeeks-website
mylist = mystr.split('-')
print(mylist)       #['Welcome', 'to', 'likegeeks', 'website']

print('-----------------------------------------------------')

#Puedes unir los elementos de la lista para hacer una cadena utilizando el método join de esta manera:
print('ejemplo 21')
mylist = ['Welcome', 'to', 'likegeeks', 'website']
print(mylist)       #['Welcome', 'to', 'likegeeks', 'website']
delimiter = ' '
output = delimiter.join(mylist)
print(output)       #Welcome to likegeeks website


#Ejemplos varios
print('--------------------------------------------')
print('Ejemplos varios')

lista1 = ['uno', 2, True]  # declara una lista heterogénea
lista2 = [1, 2, 3, 4, 5]  # declara lista numérica (homogénea)
lista3 = ['nombre', 'ap1', 'ap2']  # declara lista de strings
lista4 = [54,45,44,22,0,2,99]  # declara una lista numérica
print('lista1',lista1)
print('lista2',lista2)
print('lista3',lista3)
print('lista4',lista4)

print(lista1[0])  # uno, muestra el primer elemento de la lista
print(lista2[-1])  # 5, muestra el último elemento de la lista

print(type(lista1)) #<class 'list'

lista1[2] = False  # cambia el valor de un elemento de la lista
print('lista1 modificada',lista1)


lista2.pop(0)  # borra elemento indicado o último si no indica
print('lista2 modificada',lista2)
lista1.remove('uno')  # borra el primer elemento que coincida
print('lista1 modificada',lista1)
del lista2[1]  # borra el segundo elemento (por índice)
print('lista2 modificada',lista2)


lista2.append(7)  # añade un elemento al final con append()
print('lista2 modificada',lista2)
lista2.extend([8, 9])  # extiende lista con otra por el final
print('lista2 modificada',lista2)
lista1.insert(1, 'dos')  # inserta nuevo elemento en posición
print('lista1 modificada',lista1)
del lista2[0:3]  # borra los elementos desde:hasta
print('lista2 modificada',lista2)
lista2[:] = []  # borra todos los elementos de la lista
print('lista2 modificada',lista2)
print(lista1.count(2))  # cuenta el nº de veces que aparece 2
print(lista1.index("dos"))  # busca posición que ocupa elemento

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print("ordena la lista",sorted(thislist))  #None!!
thislist.sort()
print("ordena la lista",thislist)       #['banana', 'kiwi', 'mango', 'orange', 'pineapple']

listOrder = [54,45,44,22,0,2,99]
listOrder.sort(reverse = True)
print(listOrder)  #[99, 54, 45, 44, 22, 2, 0]

list = [54,45,44,22,0,2,99]
listOrdered = sorted(list)
print('Lista ordenada', listOrdered) #Lista ordenada [0, 2, 22, 44, 45, 54, 99]

thislist2 = ["apple", "banana", "cherry"]
if "apple" in thislist2:
  print("Yes, 'apple' is in the fruits list") #Yes, 'apple' is in the fruits list