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

#Pedimos los datos del cliente
print("Telefónica La Ladrona.SL")
print()
print("Nombre y apellidos: ")
name = input()
print()
print("Dirección: ")
direccion = input()
print()
print("Tfno: ")
tfno = input()
print()
print("Num llamadas al mes: ")
num_llamadas = input()

#LOS GUARDAMOS EN UN ARCHIVO

#Se crea y se abre el archivo para escritura
f = open("cliente_Profe.txt", "w")

#Se escriben los datos linea a linea
f.write("Nombre y Apellidos: " + name + '\n')
f.write("Dirección: " + direccion + '\n')
f.write("Tfno: " + tfno + '\n')
f.write("Num llamadas al mes: " + num_llamadas + '\n')

#Cierra el archivo
f.close()




