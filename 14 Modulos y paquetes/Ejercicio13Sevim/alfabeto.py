#!/usr/bin/env python
def alfabetizar():
    """
    Funcion para comprobar si la letra del DNI es valida.
    'letraEntrada1' es el ultimo caracter de la cadena introducida
    'testigo' es una variable para contar las veces que la letra de entrada no coincide con los elementos de la tupla
    con 'depurar.entrada[]' se llama a la variable global creada en el moduo 'depurar'
    Creamos una tupla con las letras permitidas.
    Si la letra del DNI coincide con algun elemento de la tupla la funcion termina
    Si la letra no coincide con al menos un elemento de la tupla, se sale del programa con mensaje de letra no valida
    """
    letrasValidas1 = ('T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E')
    import depurar
    letraEntrada1 = depurar.entrada[-1]
    testigo = 0
    for i in letrasValidas1:
        if letraEntrada1 == i:
            return()
        else:
            testigo += 1
    if testigo > 0:
        print(f"La letra \'{depurar.entrada[-1]}\' no es valida.")
        exit()