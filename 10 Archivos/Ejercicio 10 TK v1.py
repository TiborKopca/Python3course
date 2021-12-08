'''
Una compañía telefónica necesita la siguiente información de cada cliente para emitir su recibo:
Nombre, dirección, numero de tfno y cantidad de llamadas realizadas al mes.

Si la cantidad de llamadas no excede de 50, la tarifa por llamada es de 0.50€
Si fueran mayor que 50 pero no excede a 150 la tarifa por llamada adicional es de 0.30€
Finalmente, si la cantidad de llamadas fuera mayor de 150 la tarifa por llamada adicional es de
0.20€

Crear un programa que guarde en el archivo cliente.txt los datos del cliente (nombre, dirección, numero de tfno y cantidad de llamadas realizadas al mes)

Crear un segundo programa que leyendo los datos del archivo cliente.txt genere la factura.

Los resultados se mostraran por pantalla y se guardaran en el archivo factura.txt, se pide mostrar los
datos del cliente, el desglose de las llamadas y el importe a pagar.
'''


#import module for clearing the screen
import os
#About
os.system('clear')#this is only for Linux, if this code fails in Windows, put it in comment
print('-------------------------------------------------------------------------------')
print("Programa guarda datos de cliente y mostrara la factura.")
print('-------------------------------------------------------------------------------')

#VARIABLES
line = '-------------------------------------------------------------------------------'
fileClientes = 'Ejercicio10_cliente.txt'
fileFactura = 'Ejercicio10_factura.txt'

inputWriteOrRead = input('\
    Para guardar dator pulsa : 1 \n\
    Para leer datos y imprimir factura pulsa : 2\n\
    Para salir pulsa qualquiera \n\
    >')

while True: #will always go into loop
    if inputWriteOrRead == '1':
        nombreCliente = input('Introduzca el nombre del cliente:')
        direccionCliente = input('Introduzca la direccion del cliente:')
        numeroTelefonoCliente = input('Introduzca el numero de telefono del cliente:')
        candidadLlamadasCliente = int(input('Introduzca candidad de llamadas (en este mes) del cliente:'))

        #variable Tarifa will change acording to input how many calls had client
        if candidadLlamadasCliente <= 50 and candidadLlamadasCliente > 0:
            TARIFA = 0.5
        elif candidadLlamadasCliente >= 51 and candidadLlamadasCliente <= 150:
            TARIFA = 0.3
        elif candidadLlamadasCliente > 150:
            TARIFA = 0.2
        else :
            TARIFA = 1  #if error, we put 1 to not break the formula

        #Open the file
        fileWrite = open(fileClientes,'w+') #if doesnt exist, we create it, for reading we need to add "+"

        #Writing the data as list
        listOfData = [nombreCliente,direccionCliente,numeroTelefonoCliente,str(candidadLlamadasCliente),str(TARIFA)]

        #We add new line ('\n')to the each entry in list
        i = 0
        while i < len(listOfData):
            listOfData[i] = listOfData[i]+'\n'
            i += 1
        #print(listOfData)

        #Writing list/array to the file
        fileWrite.writelines(listOfData)
        #Go to the start of the file
        fileWrite.seek(0)

        # wholeArchive = fileWrite.readlines() #will read all the lines in the file and will create a list from it
        # print(wholeArchive) #['atawet\n', 'asd 42\n', '4242\n', '23\n', '0.5\n']

        print(line)
        print(fileWrite.read())
        print(line)

        #Closing file
        fileWrite.close()
        if fileWrite.closed:
            print("El archivo se ha cerrado correctamente.")
        else:
            print("El archivo permanece abierto.")
        break

    #READ THE FILE AND PRINT THE INVOICE
    elif inputWriteOrRead == '2':
        #Open the file
        fileRead = open(fileClientes,'r')
        content = fileRead.read()
        endOfFile = fileRead.tell()
        # print(content)
        print('Hay',endOfFile,'caracteres en el archivo.')
        fileRead.seek(0)


        #reading data from client file and putting them into variables to be used in invoice file
        nombreCliente = fileRead.readline()
        direccionCliente = fileRead.readline()
        numeroTelefonoCliente = fileRead.readline()
        candidadLlamadasCliente = int(fileRead.readline())
        tarifa = float(fileRead.readline())

        #formula to count the sum
        totalPagar = float(candidadLlamadasCliente * tarifa)

        listOfData = [
            f'Nombre del cliente:{nombreCliente}',
            f'Direccion del cliente:{direccionCliente}',
            f'Numero de telefono del cliente:{numeroTelefonoCliente}',
            f'Candidad de llamadas:{str(candidadLlamadasCliente)} \n',
            f'Suma total a pagar:{str(totalPagar)}EUR'
            ]

        #Generating invoice
        fileFactura = open(fileFactura,'w+')
        print(line)
        invoiceData = ['Imprimacion de la factura del cliente. \n',line + '\n']
        fileFactura.writelines(invoiceData)
        fileFactura.writelines(listOfData)
        fileFactura.seek(0)
        for oneLine in fileFactura.readlines():
            print(oneLine)

        print(line)
        fileFactura.close()
        fileRead.close()
    else :
        break
print('Programa termina. Ten un buen dia.')

