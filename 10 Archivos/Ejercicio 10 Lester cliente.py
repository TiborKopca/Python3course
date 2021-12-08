# Una compañía telefónica necesita la siguiente información de cada cliente para emitir su recibo:
# Nombre, dirección, numero de tfno y cantidad de llamadas realizadas al mes.
# Si la cantidad de llamadas no excede de 50, la tarifa por llamada es de 0.50€
# Si fueran mayor que 50 pero no excede a 150 la tarifa por llamada adicional es de 0.30€
# Finalmente, si la cantidad de llamadas fuera mayor de 150 la tarifa por llamada adicional es de
# 0.20€
# Crear un programa que guarde en el archivo cliente.txt los datos del cliente (nombre, dirección,
# numero de tfno y cantidad de llamadas realizadas al mes)


# INICIO


# En teoría el programita estaría hecho con solo las 9 primeras sentencias...

# Introducimos los datos del cliente
nombre = input("\nNombre y apellidos del cliente:\n")
direccion = input(f"Dirección del cliente {nombre}:\n") + "\n"
telefono = input(f"Nº de teléfono del cliente {nombre}:\n") + "\n"
llamadas = input(f"Cantidad de llamadas en el mes del cliente {nombre}:\n")
nombre = nombre + "\n"

# Creamos el archivo y en él guardamos esos datos del cliente
    # VERSIÓN normal: Sobreescribimos los datos en un archivo (cliente.txt)
clienteTXT = open("cliente.txt", "w")
datoscliente = [nombre, direccion, telefono, llamadas]
clienteTXT.writelines(datoscliente) # writelines permite iteración. 'f' un truco para salto de linea
clienteTXT.close()
    # VERSIÓN extra: Sobreescribimos los datos en archivo (clienteCAMPOS.txt) y agregaremos un Campo a cada línea
camposdatos = [("Cliente:", nombre), ("Dirección:", direccion), ("Teléfono:", telefono), ("Llamadas:", llamadas)]
open("clienteCAMPOS.txt", "w")
clienteCAMPOStxt = open("clienteCAMPOS.txt", "a")
for campo, dato in camposdatos:
    clienteCAMPOStxt.write(campo)
    clienteCAMPOStxt.write(dato)
clienteCAMPOStxt.close()

# En principio no nos lo piden, pero por si ayuda, imprimimos en pantalla lo grabado en cliente.txt
    # versión normal:
clienteTXT = open("cliente.txt") #Si en el open no especificamos modo de apertura, por defecto será modo lectura "r".
print("\nVERSIÓN NORMAL")
print("Los datos del cliente son:")
print(clienteTXT.read())
clienteTXT.close()
print("¿Cerrado?", clienteTXT.closed)
    # versión extra:
clienteCAMPOStxt = open("clienteCAMPOS.txt")
print("\nVERSIÓN CAMPOS")
print("Los datos son:")
print(clienteCAMPOStxt.read())
clienteCAMPOStxt.close()
print("Cerrado?", clienteCAMPOStxt.closed)

# FIN
