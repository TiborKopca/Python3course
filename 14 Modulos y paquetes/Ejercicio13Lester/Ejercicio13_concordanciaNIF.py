# El Ministerio del Interior desea realizar una actualización del programa para la validación del
# DNI español.
# Hay que rehacer el programa del ejercicio 12 utilizando el paradigma de la programación
# Modular.
# Cada una de las funciones ira dentro de un módulo.
# Se desarrollará una función nueva que tome el numero introducido por el usuario y lo devuelva
# en MAYÚSCULAS con los espacios en blanco, los puntos, los guiones y los guiones bajos que el
# usuario introduzca junto con el número del DNI ELIMINADOS.
# El programa principal importara los módulos y ejecutara las funciones.


def concordancia_DNI_LETRA(nif, LONGITUD_NIF, DIVISOR_NIF, TUPLA_CONCORDANCIA):
    ''' Esta Función revisa que la letra correspondiente al resto (de la
    división del DNI entre 23) coincida con la letra de ese último carácter del
    NIF introducido.'''



    # Busca la posición/elemento de la tupla (variable constante
    # TUPLA_CONCORDANCIA) según el 'resto' de la división del DNI por 23, para
    # obtener el valor de dicho elemento, y compararlo con el valor del último
    # caracter del Nif introducido. Deben coincidir para estar Ok.
    if TUPLA_CONCORDANCIA[int(nif[0:LONGITUD_NIF - 1]) % DIVISOR_NIF] == nif[LONGITUD_NIF - 1]:
        # Si coincidieron, entonces esta Función(revisión) retorna asignando (a
        # la variable global ('MensajeErrorNif') con la que se asignó la llamada
        # a esta Función) el texto...
        return f"Tu NIF: {nif} tiene nuestra validación.\n"

    # Si no ha retornado con el anterior texto (si no se ha cumplido, por tanto,
    # esa condición), así que esta revisión retorna ahora asignando (a dicho
    # valor de siempre: 'MensajeErrorNif') el texto...
    return f"Tu NIF {nif} apesta a falso. Revisa los números y la letra."
