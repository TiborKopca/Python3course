# Una compañía telefónica necesita la siguiente información de cada cliente para emitir su recibo:
# Nombre, dirección, numero de tfno y cantidad de llamadas realizadas al mes.
# Si la cantidad de llamadas no excede de 50, la tarifa por llamada es de 0.50€
# Si fueran mayor que 50 pero no excede a 150 la tarifa por llamada adicional es de 0.30€
# Finalmente, si la cantidad de llamadas fuera mayor de 150 la tarifa por llamada adicional es de
# 0.20€
# Crear un programa que leyendo los datos del archivo cliente.txt genere la factura. Los
# resultados se mostraran por pantalla y se guardaran en el archivo factura.txt, se pide mostrar los
# datos del cliente, el desglose de las llamadas y el importe a pagar.


# INICIO

# Introducir los tramos de tarifas, y los precios de las tarifas. Todas son variables numéricas.
finTramo1, finTramo2 = 50, 150
tarifa1, tarifa2, tarifa3 = 0.50, 0.30, 0.20

# Obtenemos los datos del cliente guardados en el archivo cliente.txt
datoscliente = open("cliente.txt") # Abrir archivo
nombre = datoscliente.readline() # Todos los datos incluyen salto de línea excepto el último que será la variable 'llamadasSTR'
direccion = datoscliente.readline()
telefono = datoscliente.readline()
llamadasSTR = datoscliente.readline() # Este es el total de llamadas realizadas. Ojo: es de tipo alfanumérico.
datoscliente.close() # Cerrar archivo

llamadas = int(llamadasSTR) # Necesitamos su variable de tipo numérico y ahora operar...

# Calcular/contar las llamadas que hay para cada tramo/tarifa
if llamadas <= finTramo1: # Solo hay llamadas de tarifa 1. No hay llamadas de tarifa 2 ni 3.
    llamadasTarifa2, llamadasTarifa3 = 0, 0
    llamadasTarifa1 = llamadas
else:
    llamadasTarifa1 = finTramo1
    if llamadas <= finTramo2: # Hay llamadas de tarifa 1 y 2. No hay llamadas de tarifa 3.
        llamadasTarifa3 = 0
        llamadasTarifa2 = llamadas - finTramo1
    else: # hay llamadas de tarifa 1, 2 y 3.
        llamadasTarifa2 = finTramo2 - finTramo1
        llamadasTarifa3 = llamadas - finTramo2

# Sabiendo cuántas llamadas realizadas para cada tarifa/tramo, podemos calcular el importe para cada tarifa/tramo.
importeTarifa1 = round(llamadasTarifa1 * tarifa1, 2)
importeTarifa2 = round(llamadasTarifa2 * tarifa2, 2)
importeTarifa3 = round(llamadasTarifa3 * tarifa3, 2)
    # Y así el Total final...
TOTAL = importeTarifa1 + importeTarifa2 + importeTarifa3

# Mostrar los datos de cliente y los desgloses de llamadas con sus importes a pagar.
    # Mostramos los datos generales del cliente...
print(f"\nCliente: {nombre}", end="")
print(f"Con domicilio/dirección: {direccion}", end="")
print(f"\nCon el teléfono: {telefono}", end="")
print(f"Ha realizado " + llamadasSTR + " llamadas en el mes.")

print(f"\nDE LAS CUALES:\n")

    # Y mostramos los desgloses de sus totales y del Total final
print(str(llamadasTarifa1) + " llamadas\t--> Tarifa de " + str(tarifa1) + "€/llamada  --> Total: " + str(round(importeTarifa1, 2)) + " €")
print(str(llamadasTarifa2) + " llamadas\t--> Tarifa de " + str(tarifa2) + "€/llamada  --> Total: " + str(round(importeTarifa2, 2)) + " €")
print(str(llamadasTarifa3) + " llamadas\t--> Tarifa de " + str(tarifa3) + "€/llamada  --> Total: " + str(round(importeTarifa3, 2)) + " €")
print("\n\t\t\t\t\t    --> Total: " + str(round(TOTAL, 2)) + " €\n")

# Crear archivo factura.txt y grabar los datos en él.
archivofactura = open("factura.txt", "w") # Crea o sobreescribe factura.txt

    # Grabamos en factura.txt los datos generales del cliente.
archivofactura.write(f"Cliente:{nombre}")
archivofactura.write(f"Dirección:{direccion}")
archivofactura.write(f"Teléfono:{telefono}")
archivofactura.write(f"Total Llamadas:{llamadasSTR}\n")

    # Y grabamos también cada desglose (los subtotales no importan pues se podría recalcular con estos datos grabados...)
archivofactura.write("Llamadas Tarifa 1:\n") # Cada concepto grabado en 1 línea del archivo factura.txt
archivofactura.write(f"{llamadasTarifa1}\n") # Y su valor (el de cada concepto) también en 1 línea.
archivofactura.write("Precio Tarifa 1:\n")
archivofactura.write(f"{tarifa1}\n")
archivofactura.write("Llamadas Tarifa 2:\n")
archivofactura.write(f"{llamadasTarifa2}\n")
archivofactura.write("Precio Tarifa 2:\n")
archivofactura.write(f"{tarifa2}\n")
archivofactura.write("Llamadas Tarifa 3:\n")
archivofactura.write(f"{llamadasTarifa3}\n")
archivofactura.write("Precio Tarifa 3:\n")
archivofactura.write(f"{tarifa3}\n")

    # Por último, sí grabo... el Total final.
archivofactura.write("IMPORTE TOTAL:\n")
archivofactura.write(str(round(TOTAL, 2)))

archivofactura.close() # Cierra el archivo factura.txt

