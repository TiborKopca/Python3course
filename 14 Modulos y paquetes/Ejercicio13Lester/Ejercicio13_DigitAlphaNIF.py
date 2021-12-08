# El Ministerio del Interior desea realizar una actualización del programa para la validación del
# DNI español.
# Hay que rehacer el programa del ejercicio 12 utilizando el paradigma de la programación
# Modular.
# Cada una de las funciones ira dentro de un módulo.
# Se desarrollará una función nueva que tome el numero introducido por el usuario y lo devuelva
# en MAYÚSCULAS con los espacios en blanco, los puntos, los guiones y los guiones bajos que el
# usuario introduzca junto con el número del DNI ELIMINADOS.
# El programa principal importara los módulos y ejecutara las funciones.


def revisaDigitAlpha(nif, LONGITUD_NIF):
    ''' Esta Función revisa que todos los caracteres sean dígitos, y que el
    último caracter sea una letra.'''

    # Revisa uno a uno toda la longitud del NIF (excepto el último carácter, es
    # decir: hasta el penúltimo carácter), que cada caracter sean un dígito.
    for n in range(LONGITUD_NIF - 1):

        # Si el caracter de la posición 'n' no es un dígito (caracter numérico).
        if nif[n].isdigit() == False:
            # entonces retorna con este texto de error...
            return f"La posición {n + 1} del NIF {nif} contiene el caracter '{nif[n]}', pero debería ser algún número del 0 al 9."
        # De lo contrario (si sí es un dígito) entonces comprueba el siguiente
        # caracter (posición) del nif ('for n in...') y así hasta el penúltimo
        # caracter de la longitud del nif: 'range(LONGITUD_NIF - 1)'

    # Si completó el anterior 'for n in...' es que todos fueron dígitos (ok), y
    # entonces ahora revisa solo el último caracter para saber si éste es, o no,
    # alguna letra.
    # Si el último caracter no es 'alpha' (si no es una letra)...
    if nif[LONGITUD_NIF - 1].isalpha() == False:
        # entonces retorna con este texto de error...
        return f"El último caracter del NIF {nif} ha de ser una letra en vez de '{nif[n + 1]}'."
    
    # Si no ha retornado antes, entonces es que el último carácter era una Letra
    # y entonces esta revisión retorna asignando (a la variable global con la
    # que se asignó la llamada a esta Función) el texto...
    return "OkDigitAlpha."
