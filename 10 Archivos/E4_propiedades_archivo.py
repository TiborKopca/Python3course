#Abrimos el archivo para lectura
file = open("demo.txt","r")

#Vemos sus propiedades
nombre = file.name
modo = file.mode
codificacion = file.encoding

print('El archivo se llama: ', nombre) #El archivo se llama:  demo.txt
print('Esta abierto en modo: ', modo) #Esta abierto en modo:  r
print('Esta codificado en modo: ', codificacion)  #Esta codificado en modo:  UTF-8

#Cerramos el archivo
file.close()

#Comprobamos si el archivo se ha cerrado correctamente
if file.closed:
    print('El archivo se ha cerrado correctamente')
else:
    print('El archivo permanece abierto')
