#!/usr/bin/env python
#Este modulo depura el DNI introducido de las impurezas como 
#espacios en blanco, los puntos, los guiones y los guiones bajos
#aqui se crea la variable global 'entrada' para usarl en los otros modulos
def limpieza():
    '''
    Esta funcion recoge la entrada del usuario y quita de ella los espacio blancos, 
    los puntos, las comas,  los guiones y los guiones bajos
    La variable 'entrada' es global y se usa en los demas modulos
    '''
    global entrada
    entradaUsuario = input("Su DNI, por favor: ")
    entrada = entradaUsuario.replace(" ", "").replace(".", "").replace("-", "").replace("_", "").replace(",", "").upper()