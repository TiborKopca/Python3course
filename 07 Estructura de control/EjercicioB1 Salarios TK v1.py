"""
B1) Una empresa tiene trabajadores de categorías A, B y C.
Los de categoría A cobran 1.500€ mensuales.
Los de categoría B cobran 1000€ mensuales.
Los de categoría C cobran 650€ mensuales.

Cobran todos un suplemento de 240€ , excepto los de categoría C.
De éstos en la sección 1a están los contratados por días, que cobran un suplemento de 0,5€ por día trabajado y se les descuenta 30€ por día de baja injustificada.
El resto de las secciones de esta categoría (2a, 3a y 4a) cobra 120€ por suplemento.

El jefe de contabilidad de la empresa nos ha encargado un programa para calcular los salarios de los
empleados de la compañía. Este programa debería aceptar el numero de la seguridad social de un
empleado, su nombre y apellidos, la categoría y la sección a la que pertenece.
Para cada empleado el programa debe mostrar en pantalla: su nombre y apellidos, su número de la
seguridad social, la categoría y la sección a la que pertenece y su salario.
"""

#import module for clearing the screen
import os
#About
os.system('clear')#this is only for Linux, if this code fails in Windows, put it in comment
print('-------------------------------------------------------------------------------')
print("Programa para calcular los salarios de los empleados segun criterios.")
print("Es necesario entrar datos - Nombre, Apellido, Numero de la seguridad social, \nLa Categoria y La seccion a la que pertenece el empleado.")
print('-------------------------------------------------------------------------------')

#VARIABLES
nombreEmpleado = ''
apellidoEmpleado = ''
nSeguridadSocial = 0
categoria = ""          #A,B,C,D
seccion = ''            #1, 2, 3, 4
salario = 0
diasTrabajando = 0
end = -1
output = ''
endMessage = "Pulsa cualquiera para continuar y hacer mas calculaciones.\nPulsa 0 para salir."
errorFlag = False
#CONSTANTES
SUPLEMENTO_AB = 240
SUPLEMENTO_C = 120
SALARIO_A = 1500
SALARIO_B = 1200
SALARIO_C = 600
SALARIO_C_DIA = 0.5
DESCUENTA_BAJA = 30

#Input data from the user
while end != '0':
    nombreEmpleado = input("Introduzca nombre del Empleado:")
    apellidoEmpleado = input("Introduzca apellido del Empleado:")
    nSeguridadSocial = input("Introduzca numero de Seguridad Social del Empleado:")
    categoria = input("Introduzca la categoria del Empleado(A,B,C):")
    seccion = input("Introduzca la seccion del Empleado(1,2,3,4):")

    if (categoria == "c" or categoria == "C") and seccion == '1':
        nDiasTrabajando = float(input('Cuantos dias ha trabajado?:'))
        nBajas = float(input('Introduzca días de baja injustificada:'))

    #Calculations
    if categoria == 'A' or categoria == 'a':
        salario = SALARIO_A + SUPLEMENTO_AB
    elif categoria == 'B' or categoria == 'b':
        salario = SALARIO_B + SUPLEMENTO_AB
    elif categoria == 'C' or categoria == 'c':
        if seccion == '1':
            salario = SALARIO_C + (nDiasTrabajando * SALARIO_C_DIA) - (nBajas * DESCUENTA_BAJA)
        elif seccion == '2' or seccion == '3' or seccion == '4':
            salario = SALARIO_C + SUPLEMENTO_C
        else:
            output = f'No hay categoria {seccion} que has indicado, intentalo de nuevo.'
            errorFlag = True
    else:
        output = f'No hay categoria {categoria} en la empresa, intentalo de nuevo.'
        errorFlag = True

    #No hubo errores
    if errorFlag == False:
        output = f"Empleado :{nombreEmpleado.title()} {apellidoEmpleado.title()} con #Seg.Social:{nSeguridadSocial} tiene salario {salario}€, cual pertenece a la categoria:{categoria} seccion:{seccion}."

    #Output
    print("--------------------------------------------------------")
    print(output)
    print("--------------------------------------------------------")
    print(endMessage)

    end = input()  #user wants to end - we break out of loop while
    salario = 0         #for the next calculations reset the variable
    errorFlag = False   #reset the flag
print('Fue un placer, el programa termina.')

