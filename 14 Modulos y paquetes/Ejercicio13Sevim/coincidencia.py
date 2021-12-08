#!/usr/bin/env python
def validacion():
    """
    Funcion para comprobar si la letra del DNI corresponde al numero introducido
    'numDNI' es la parte numerica del DNI
    'letraEntrada2' es la letra del DNI
    'restoDiv' es el resto de la division del numero del DNI por 23
    Se crea un tupla, aprovechando que el indice de cada elemento puede servir como el numero correspondiente para esta letra.
    Se compara la letra del DNI con el elemento de la tupla con indice el resto de la division de
    la parte numerica del DNI por 23. Si coinciden, la funcion termina y si no 
    coinciden, se sale del programa con el mensaje de combinacion no valida.
    con 'depurar.entrada[]' se llama a la variable global creada en el moduo 'depurar'    
    """
    import depurar
    letraEntrada2 = depurar.entrada[8]
    numDNI = int(depurar.entrada[0:8])
    restoDiv = numDNI % 23
    letrasValidas2 = ('T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E')
    if letrasValidas2[restoDiv] != letraEntrada2:
        print(f"La combinacion de caracteres \'{depurar.entrada}\' no es valida.")
        exit()
    else:
        return()