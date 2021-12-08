#Creamos el archivo
f = open("archivo.txt", "w+")
content = f.read() #reads all the characters
endOfFile = f.tell() #after being on end, we store the end character.
print('End of file is now',f.tell()) #0
cadena1 = 'Las rosas son rojas \n'
cadena2 = 'Las margaritas blancas \n'

#Escribimos una cadena de texto
f.write(cadena1)
#Escribimos otra cadena de texto
f.write(cadena2)

#Vemos la posicion actual del puntero
print('Posición actual del puntero al cerrar el archivo:')
print(f.tell())

endOfFile = f.tell()
print('End of file is now',f.tell()) #0

#Cerramos el archivo
f.close()

#Abrimos el archivo para añadir contenido y lectura
archivo = open("archivo.txt", "a+")

#Vemos la posicion actual del puntero
print('Posición actual del puntero al abrir el archivo:')
print(archivo.tell())

#Creamos una lista
lista = ['lunes \n', 'martes \n', 'miercoles \n', 'jueves \n', 'viernes \n', 'sabado \n', 'domingo \n']
#Escribimos la lista en el archivo añadiendo salto de linea
archivo.writelines(lista)

#Vemos la posicion actual del puntero
print('Posición actual del puntero es:')
print(archivo.tell())

#Llevamos el puntero al principio
archivo.seek(0)

#Vemos el contenido del fichero
print(archivo.read())

#Cerramos el archivo
archivo.close()

