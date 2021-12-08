#!/usr/bin/env python
def recorte():
    """
    Funcion para comprobar la longitud de la cadena introducida por el usuario
    'numCaracteres' es la cantidad de caracteres del DNI introducido
    con 'depurar.entrada[]' se llama a la variable global creada en el moduo 'depurar'
    Si son 9 caracteres la funcion termina y si no, sale del programa.
    """
    import depurar
    numCaracteres = len(depurar.entrada)
    if numCaracteres != 9:
        print(f"El numero introducido no es valido. Ha introducido {numCaracteres} caracteres y se necesitan 9.")
        exit()
    else:
        return()