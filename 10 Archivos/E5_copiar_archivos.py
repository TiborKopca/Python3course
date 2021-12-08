#El ejemplo siguiente abre un fichero y lo copia en otro

#El archivo se abre por defecto en modo lectura
f = open("demo.txt")

#El otro archivo en modo escritura
g = open("destino.txt", "w")

#Leemos linea a linea en el fichero de origen
#y lo escribimos en el fichero de destino
for linea in f:
    g.write(linea)

#Cerramos los ficheros
g.close()
f.close()
