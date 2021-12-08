'''10) Una compañía telefónica necesita la siguiente información de cada cliente para emitir su recibo:
Nombre, dirección, numero de tfno y cantidad de llamadas realizadas al mes.
Si la cantidad de llamadas no excede de 50, la tarifa por llamada es de 0.50€
Si fueran mayor que 50 pero no excede a 150 la tarifa por llamada adicional es de 0.30€
Finalmente, si la cantidad de llamadas fuera mayor de 150 la tarifa por llamada adicional es de
0.20€
Crear un programa que guarde en el archivo cliente.txt los datos del cliente (nombre, dirección,
numero de tfno y cantidad de llamadas realizadas al mes)
Crear un segundo programa que leyendo los datos del archivo cliente.txt genere la factura. Los
resultados se mostraran por pantalla y se guardaran en el archivo factura.txt, se pide mostrar los
datos del cliente, el desglose de las llamadas y el importe a pagar. '''

#LEEMOS LOS DATOS DEL ARCHIVO cliente.txt
# Abre archivo en modo lectura
archivo = open('cliente_Profe.txt','r')

#Leemos el archivo linea a  linea y lo guardamos en una lista
mycliente = archivo.readlines()
print(mycliente) #['tibor\n', 'sagasta 12\n', '04535326\n', '423']
#Cerramos el archivo
archivo.close()

#OBTENEMOS LAS LLAMADAS REALIZADAS
#Averiguamos la cantidad de llamadas realizadas
llamadas = mycliente[3]
#Quitamos los espacios en blanco al inicio y al final de la cadena
llamadas = llamadas.strip()
#Obtenemos la posición de :
indice = llamadas.find(":")
#Obtenemos la parte de la cadena que contiene el num de llamadas
myllamadas =llamadas[indice+1:]
#Lo pasamos a entero
numLlamadas = int(myllamadas)

#CALCULAMOS LA CANTIDAD A PAGAR

if numLlamadas <= 50:
    precio = numLlamadas * 0.50
elif numLlamadas > 50 and numLlamadas <= 150:
    precio1 = 50 * 0.50
    precio2 = (numLlamadas - 50) * 0.30
    precio = precio1 + precio2
elif numLlamadas > 150:
    precio1 = 50 * 0.50
    precio2 = 100 * 0.30
    precio3 =(numLlamadas - 150) * 0.20
    precio = precio1 + precio2 + precio3


#GUARDAMOS LOS DATOS EN EL ARCHIVO factura.txt

#Creamos el archivo y lo abrimos en modo escritura
file = open("factura_Profe.txt", "w")

#Escribimos varias lineas
file.write("FACTURA" + "\n")
file.write("\n") #Linea en blanco
file.write("Telefónica La Ladrona.SL" + "\n")
file.write("-------------------------" + "\n")
file.write("\n")
file.write("\n")

#Leemos los datos del archivo cliente.txt que hemos guardado en una lista
#los leemos de la lista y los escribimos en el archivo factura.txt
file.writelines(mycliente)
file.write("\n")

#Añadimos una nueva linea con el total a pagar
file.write("TOTAL A PAGAR: " + str(precio) + "\n")

#Cerramos el archivo
file.close()

#PRESENTAR LOS DATOS EN PANTALLA
#Abrimos el archivo en modo lectura
with open("factura.txt", "r") as f:
    print(f.read())










