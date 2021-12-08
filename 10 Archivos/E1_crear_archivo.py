#Creamos un archivo de texto
file = open("demo.txt","w")

#Escribimos en el
file.write('Hola mundo'+ '\n') 
file.write('Estamos escribiendo en un archivo de texto.' + '\n') 
file.write('Esta es la tercera linea' + '\n') 
file.write('Esta es la ultima linea.' + '\n')

#Cerramos el archivo
file.close()
