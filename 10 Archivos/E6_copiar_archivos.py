'''
El ejemplo siguiente abre un fichero y lo copia en otro.
Hace la copia del fichero leyendo con readline() en un bucle hasta fin de fichero.
Cuando lleguemos a final de fichero nos devolverá una línea vacía.
'''

#El archivo se abre por defecto en modo lectura
f = open("destino.txt")

#El otro archivo en modo escritura
g = open("destino2.txt", "w")

#Lee con readline() en un bucle hasta fin de fichero.

#Lee la primera linea
linea = f.readline()

#Lee las siguentes lineas mientras haya lineas que leer
while linea != "":
    g.write(linea)
    linea = f.readline()

#Cerramos el fichero
g.close()
f.close()
