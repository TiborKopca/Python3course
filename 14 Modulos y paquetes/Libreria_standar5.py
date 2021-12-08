'''El módulo os nos va a permitir interactuar con el sistema operativo y
manejar todas aquellas funcionalidades que ofrece.'''

'''El módulo shutil nos va a permitir administrar ficheros de forma
sencilla.'''

import os
import shutil

print("Directorio de trabajo actual: ",os.getcwd()) #Directorio de trabajo actual:  /home/teamkk/Downloads/PYTHON

print('---------------------------------------------------------')

print('El contenido del directorio actual es: ', os.listdir("./"))
#El contenido del directorio actual es:
# ['01 Algoritmos', 'archivo.txt', '14 Modulos y paquetes', '06 Entrada y Salida standard', 'Ejercicio10_factura.txt', '13 Programacion modular', '11 Errores y Exceptiones', '09 Estructuras de datos', '10 Archivos', 'nuevofilename.txt', '02 Lenguajes de programacion', 'notas.txt', '05 Elementos de un programa', 'Ejercicio10_cliente.txt', '07 Estructura de control', 'filename.txt', '03 Paradigmas de programacion', '12 Funciones', 'Ejercicio9_notas.txt', '08 Variables y tipo de datos', 'demo.txt', '04 Python', 'clienteCAMPOS.txt']

#Creamos un archivo
file = open("filename.txt", "w")
file.write("Primera línea" + os.linesep) #os.linesep te permitirá obtener los caracteres necesarios para crear el salto de línea de acuerdo al sistema operativo
file.write("Segunda línea")
file.close()

#realizar la copia del fichero en uno
#nuevo con el nombre especificado por parámetro.
shutil.copy("filename.txt","nuevofilename.txt")
