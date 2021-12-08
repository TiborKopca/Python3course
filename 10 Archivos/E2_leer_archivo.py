#Leer en un archivo
#Abrimos elarchivo en modo lectura
file = open("demo.txt", "r")

#extrae una cadena que contiene todos los caracteres del archivo
print('1. Lee todos los caracteres')
print()
print(file.read())
print('--------------------')
#ponemos el puntero al principio
file.seek(0)


#leerá los primeros cuatro caracteres de los datos almacenados y los devolverá como una cadena:
print('2. Lee cuatro caracteres')
print()
print(file.read(4)) #reads 4 first characters
print('--------------------')
#ponemos el puntero al principio
file.seek(0)

#devolverá una cadena de caracteres que contiene una sola línea
print('3. Lee una linea')
print()
print(file.readline()) #reads first line from the file
print('--------------------')
#ponemos el puntero al principio
file.seek(0)

#Lee todas las líneas de un archivo.
print('4. Lee todas las líneas de un archivo y las guarda en una lista ')
print()
for linea in file.readlines():
    print(linea) #reads all the lines in the file
print('--------------------')

#Retorna la posición actual del puntero.
print(file.tell()) #returns the actual position

#ponemos el puntero al principio
file.seek(0)  #move to the start of the file

#Retorna la posición actual del puntero.
print(file.tell())



# Cierra un archivo.
file.close() #closes the file

