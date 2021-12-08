#!/usr/bin/env python
#La linea anterior es aplicable solo para Linux
#Empezamos pidiendo nombre, apellidos, numero de seguridad social y la categoria que tiene el empleado.
#Tenemos tres categorias - A, B y C. Los sueldos de categorias A y B son de 1500 y 1000 mas el suplemento de 240 euros. Aqui lo tenemos claro. 
#Categoria C esta dividida en 4 secciones. Seccion 1 cobran 650 euros + 0,5 por dia. Una falta injustificada se penaliza con -30 euros.
#Un mes tiene 22 dias laborables, entonces si falta un dia sin justificacion pierde los 30 euros de penalizacion pero tambien el suplemento sera 0,5 x 21 dias.
#Secciones 2,3 y 4 de categoria C cobran 650 euros + 120 euros de suplemento.
#Si un empleado pertence a categoria A o B, entonces cobra 1500+240 o 1000+240 euros respectivamente.
#Si el empleado pertence a categoria C, entonces preguntamos si es de seccion uno o no. Si no es de seccion uno (se entiende que es de seccion 2,3 o 4), entonces
#cobra 650 euros + 120 euros. Hasta aqui bien. Si es de categoria C y seccion 1, entonces preguntamos sy ha faltado algun dia.
#El salario de categoria C seccion 1 es 650 + (22 - dias_falta_no_justificada) * 0,5 - dias_falta_no_justificada * 30 euros.
#Algo como pseudocodigo:
#Inicio
#Introduzca el nombre, apellidos, numeroSegSocial, categoria
#Si categoria = A -> imprime (El salario del empleado es 1500+240 euros )
#Elif categoria = B -> imprime (El salario del empleado es 1000+240 euros)
#Elif categoria = C -> 
#     Introduzca la seccion en la que esta el empleado , de 1 a 4, por favor
#     Si seccion > 1 -> imprime (El salario del empleado es 650 +120 euros)
#     Else -> Introduzca cuantos dias de baja injustificada tiene este empleado - faltaInjustufucada
#     Imprime (El salario del empleado es 650 + 22*0,5 - faltaInjustificada * 30 
#Else introduzca A, B o C para la categoria, por favor
# ===========Empezamos con el codigo============
#from os import system, name
#system('clear') #esto solo funcionara en Linux para Windows el comando es 'cls'
print("De momento no se hace ninguna comprobacion de los tipos y los valores de los datos introducidos. Nos fiamos de la buena fe del contable :)")
print("Para salir del programa introduzca 'abcd' para el nombre, los apellidos o la categoria del empleado. El codigo de salida para el numero de Seguridad Social es '0'.")
while True:
    print("============================================")
    print("Para salir del programa introduzca 'abcd' para el nombre, los apellidos o la categoria del empleado. El codigo de salida para el numero de Seguridad Social es '0'.")
    nombre = input("Introduzca el nombre del epmleado, por favor:")
    if nombre == 'abcd':
        print("Usted ha elegido salir del programa. Que tenga un buen dia!")
        break
#El mismo mecanismo se puede utilizar en cada entrada de datos por parte del usuario para salir del programa en cada momento. 
    apellidos = input("Introduzca los apellidos, por favor:")
    if apellidos == 'abcd':
        print("Usted ha elegido salir del programa. Que tenga un buen dia!")
        break
#Quiza el nombre y los apellidos pueden ir en una sola variable, pero ...
    segSocial = int(input("Introduzca el numero de Seguridad Social del empleado, por favor:"))
    if segSocial == 0:
        print("Usted ha elegido salir del programa. Que tenga un buen dia!")
        break
#Aqui se puede comprobar si lo introducido es numero u otra cosa. De momento nos fiamos de la buena fe del contable :)
    categoria = input("Introduzca la categoria A, B, o C, por favor:")
    if categoria == 'abcd':
        print("Usted ha elegido salir del programa. Que tenga un buen dia!")
        break
    elif categoria == 'a' or categoria == 'A':
#       system('clear') #esto solo funcionara en Linux
        print(f"El salario del empleado {nombre.title()} {apellidos.title()} con numero de Seguridad Social {segSocial} y categoria {categoria.title()}, es 1740 euros.")
    elif categoria == 'b' or categoria == 'B':
#       system('clear') #esto solo funcionara en Linux
        print(f"El salario del empleado {nombre.title()} {apellidos.title()} con numero de Seguridad Social {segSocial} y categoria {categoria.title()}, es 1240 euros.")
#La construccion nombre.title() nos permite introducir el texto sin mayusculas, pero imprimiendolo empezara siempre en mayuscula
    elif categoria == 'c':
        seccion = int(input("Introduzca la seccion a la que pertence el empleado, por favor:"))
        if seccion == 1:
            faltaInjustificada = int(input(f"Cuantos dias de falta injustificada tiene el empleado {nombre.title()} {apellidos.title()}:"))
            sueldo = 650 + ((22 - faltaInjustificada) * 0.5) - (faltaInjustificada * 30)
#           system("clear") #esto solo funcionara en Linux
            print(f"El sueldo del empleado {nombre.title()} {apellidos.title()} con numero de Seguridad Social {segSocial} y con categoria {categoria.title()}, seccion {seccion} y {faltaInjustificada} dias de falta injustificada, es  {sueldo } euros.")
        elif seccion == 2 or seccion == 3 or seccion ==4:
            sueldo = 650 + 120
#           system('clear') #esto solo funcionara en Linux
            print(f"El sueldo del empleado {nombre.title()} {apellidos.title()} con numero de Seguridad Social {segSocial} y con categoria {categoria.title()}, seccion {seccion}, es  {sueldo } euros.")
        else:
            print("La seccion introducida no es valida. Debe ser de 1 a 4, por favor.")
    else:
        print("La categoria debe ser A, B, C o D, por favor.")
