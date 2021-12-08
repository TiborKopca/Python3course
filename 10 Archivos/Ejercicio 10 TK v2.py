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
import datetime
#About
os.system('clear')#this is only for Linux, if this code fails in Windows, put it in comment
print('-------------------------------------------------------------------------------')
print("Programa guarda datos de cliente y mostrara la factura.")
print('-------------------------------------------------------------------------------')

#VARIABLES
line = '-------------------------------------------------------------------------------'
fileClientes = 'Ejercicio10_cliente.txt'
fileFactura = 'Ejercicio10_factura.txt'

while True: #will always go into loop
    inputWriteOrRead = input('\
    Para guardar dator pulsa : 1 \n\
    Para leer datos y imprimir factura pulsa : 2\n\
    Para salir pulsa qualquiera \n\
    >')

    if inputWriteOrRead == '1':
        nombreCliente = input('Introduzca el nombre del cliente:')
        direccionCliente = input('Introduzca la direccion del cliente:')
        numeroTelefonoCliente = input('Introduzca el numero de telefono del cliente:')
        candidadLlamadasCliente = int(input('Introduzca candidad de llamadas (en este mes) del cliente:'))
        dateOfCreation = datetime.datetime.now()
        # print(dateOfCreation)       #2021-11-28 16:37:07.135914
        dateOfCreation = dateOfCreation.strftime("%c") #Sun Nov 28 18:04:15 2021

        #Open the file
        fileWrite = open(fileClientes,'w+') #if doesnt exist, we create it, for reading we need to add "+"

        #Writing the data as list
        listOfData = [
            'Datos de cliente de la empresa telefonica XYZ \n',
            'Fecha de creacion de entrada de datos:'+dateOfCreation+'\n',
            nombreCliente+'\n',
            direccionCliente+'\n',
            numeroTelefonoCliente+'\n',
            str(candidadLlamadasCliente)+'\n']

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

    #READ THE FILE AND PRINT THE INVOICE
    elif inputWriteOrRead == '2':
        #Open the file CLIENTS in read mode
        dataClientes = open(fileClientes,'r')
        content = dataClientes.read()   #read all the content
        endOfFile = dataClientes.tell() #read total bytes
        # print(content)
        print()
        print(line)
        print('Estoy leyendo:',endOfFile,'caracteres en el archivo.')
        dataClientes.seek(0)

        #reading data from client file line by line and save it to the list
        clientFileList = dataClientes.readlines()
        # print(clientFileList) #['tibor\n', 'sagasta 12\n', '04535326\n', '423']

        #Closing the file CLIENTS
        dataClientes.close()

        #Reading the data from the list to be written to the facture
        dateStored = clientFileList[1]
        indexDate = dateStored.find(':')    #we find fist occurance of ":"
        dateDataOrigin = dateStored[indexDate+1:] #get the string behind the ':'

        nombreCliente = clientFileList[2]
        direccionCliente = clientFileList[3]
        numeroTelefonoCliente = clientFileList[4]
        candidadLlamadasCliente = int(clientFileList[5])

        #formula to count the sum and tarifa based on how many calls had client
        TARIFA_50 = 0.5
        TARIFA_150 = 0.3
        TARIFA_UNLIMITED = 0.2

        totalPagar = 0  #the result sum to pay by client
        if candidadLlamadasCliente <= 50 and candidadLlamadasCliente > 0:
            totalPagar = float(candidadLlamadasCliente * TARIFA_50)
        elif candidadLlamadasCliente > 50 and candidadLlamadasCliente <= 150:
            totalPagar = (50 * TARIFA_50) + float(candidadLlamadasCliente * TARIFA_150)
        elif candidadLlamadasCliente > 150:
            totalPagar = (50 * TARIFA_50) + (150 * TARIFA_150) + float(candidadLlamadasCliente * TARIFA_UNLIMITED)

        listOfData = [
            f'Nombre del cliente:{nombreCliente}',
            f'Direccion del cliente:{direccionCliente}',
            f'Numero de telefono del cliente:{numeroTelefonoCliente}',
            f'Candidad de llamadas:{str(candidadLlamadasCliente)} \n',
            f'Suma total a pagar:{str(totalPagar)}EUR'
            ]

        #Generating invoice
        file = open(fileFactura,'w+')
        print(line)
        invoiceData = [
            'Imprimacion de la factura del cliente. \n',\
            line + '\n',\
            f'Fecha de creacion de archivo con datos:{dateDataOrigin}',]
        file.writelines(invoiceData)
        file.writelines(listOfData)
        file.seek(0)
        for oneLine in file.readlines():
            print(oneLine)

        print(line)
        file.close()

    else :  #if user didnt select 1 or 2 specifically
        break
print('Programa termina. Ten un buen dia.')

