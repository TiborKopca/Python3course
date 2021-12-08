'''
Las variables en Python se crean cuando se definen por primera vez, es decir, cuando se les asigna un valor por primera vez.
Para asignar un valor a una variable se utiliza el operador de igualdad (=).
A la izquierda de la igualdad se escribe el nombre de la variable y a la derecha el valor que se quiere dar a la variable.

'''

#En el ejemplo siguiente se almacena el número decimal 2.5 en una variable de nombre x
x = 2.5
print(x)

#La variable se escribe siempre a la izquierda de la igualdad. Si se escribe al revés, Python genera un mensaje de error:

#2.5 = x
#SyntaxError: can't assign to literal

#Si una variable no se ha definido previamente, escribir su nombre genera un mensaje de error:

x = -10
print(x)
#y

#Una variable puede almacenar números, texto o estructuras más complicadas (matrices, listas, tuplaspunteros, diccionarios, etc.).
#Si se va a almacenar texto, el texto debe escribirse entre comillas simples (') o dobles ("), que son equivalentes.
#A las variables que almacenan texto se les suele llamar cadenas (de texto).

nombre = "Pepito Conejo"
print(nombre)

#Si no se escriben comillas, Python supone que estamos haciendo referencia a otra variable
#(que, si no está definida,genera un mensaje de error):

#nombre = Pepe
#nombre = Pepito Conejo

'''
Aunque no es obligatorio, se recomienda que el nombre de la variable esté relacionado con la información que se almacena en ella,
para que sea más fácil entender el programa.
El nombre de una variable debe empezar por una letra o por un guion bajo (_) y puede seguir con más letras, números o guiones bajos.
'''
_x = 3.8
print(_x)

x1 = 100
print(x1)

fecha_de_nacimiento = "27 de octubre de 1997"
print(fecha_de_nacimiento)

#Los nombres de variables no pueden incluir espacios en blanco.

#fecha de nacimiento = "27 de octubre de 1997"

'''
Los nombres de variables pueden contener cualquier carácter alfabético
(los del alfabeto inglés, pero también ñ, ç o vocales acentuadas),
aunque se recomienda utilizar únicamente los caracteres del alfabeto inglés.
'''

año = 1997
print(año)

#Los nombres de las variables pueden contener mayúsculas,
#pero tenga en cuenta que Python distingue entre mayúsculas y minúsculas
#(en inglés se dice que Python es case-sensitive).

nombre = "Pepito Conejo"
Nombre = "Numa Nigerio"
nomBre = "Fulanito Mengánez"

print(nombre)
print(Nombre)
print(nomBre)

'''
Cuando el nombre de una variable contiene varias palabras, se aconseja separarlas con guiones bajos
para facilitar la legibilidad, aunque también se utiliza la notación camelCase,
en las que las palabras no se separan pero empiezan con mayúsculas (salvo la primera palabra).
'''

fecha_de_nacimiento = "27 de octubre de 1997"
fechaDeNacimiento = "31 de marzo de 1964"

print(fecha_de_nacimiento)
print(fechaDeNacimiento)

#Las palabras reservadas del lenguaje (las que IDLE escribe en naranja) están prohibidas como nombres de variables:

#lambda = 3

'''
Los nombres de las funciones integradas sí que se pueden utilizar como nombres de variables,
pero más vale no hacerlo porque a continuación ya no se puede utilizar la función como tal
Borrando con del la variable con nombre de función, se recupera la función.
'''
print = 3
#print("Hola")
del print
print("Hola")

#La instrucción del borra completamente una variable.

nombre = "Pepito Conejo"
print(nombre)

del nombre
#print(nombre)


