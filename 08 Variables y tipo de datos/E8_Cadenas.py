#Concatenación de cadenas
str = "welcome " + "to Python"
print (str)
print()     #welcome to Python

#Multiplicación de cadenas
str = "LikeGeeks" * 2
print (str)
print()     #LikeGeeksLikeGeeks

#Buscar una subcadena
#El método find imprime la posición de la primera
#aparición de la cadena likegeeks si se encuentra.
#Si no encuentra nada, devolverá -1 como resultado.
str = "welcome to likegeeks website"
print(str.find("likegeeks"))
print()     #11

#La función de find comienza desde el primer carácter,
#sin embargo, puede comenzar desde el enésimo carácter de esta manera:
str = "welcome to likegeeks website"
print(str.find("likegeeks",12))
print()     #-1
#Como comenzamos desde el carácter 12, no hay una palabra
#llamada likegeeks desde esa posición, por lo que devolverá -1.


#Obtener subcadenas
str = "first second third"
print(str[:2])  #fi
print(str[2:])  #rst second third
print(str[3:5]) #st
print()

#Reemplazar cadenas
str = "This website is about programming"
str2 = str.replace("This", "That")
print(str2) #That website is about programming
print()

#Si tiene muchas ocurrencias y deseas reemplazar
#solo la primera, puede especificar eso:
str = "This website is about programming I like this website"
str2 = str.replace("website", "page",1)
print(str2) #This page is about programming I like this website
print()

#Puedes recortar los espacios en blanco de una cadena usando el método strip
str = "   This website is about programming    "
print(str.strip())     #This website is about programming
print()

#Puedes quitar solo los de la derecha o izquierda utilizando
#los métodos rstrip () o lstrip () respectivamente.
#Cambiar entre Caracteres en mayúscula y minúsculas
str="Welcome to likegeeks"
print(str.upper())  #WELCOME TO LIKEGEEKS
print(str.lower())  #welcome to likegeeks
print()

#Puede utilizar la funcion len ()
#para calcular la longitud total de la cadena.
str="introducción a la programación"
str='1234567890'
print(len(str)) #30
print()

#Puedes iterar sobre las cadenas y manipular cada carácter individualmente de la siguiente forma:
str="welcome to likegeeks website"
for i in range(len(str)):
    print(str[i])
