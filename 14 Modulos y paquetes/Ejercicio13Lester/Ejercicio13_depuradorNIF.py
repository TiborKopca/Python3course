# El Ministerio del Interior desea realizar una actualización del programa para la validación del
# DNI español.
# Hay que rehacer el programa del ejercicio 12 utilizando el paradigma de la programación
# Modular.
# Cada una de las funciones ira dentro de un módulo.
# Se desarrollará una función nueva que tome el numero introducido por el usuario y lo devuelva
# en MAYÚSCULAS con los espacios en blanco, los puntos, los guiones y los guiones bajos que el
# usuario introduzca junto con el número del DNI ELIMINADOS.
# El programa principal importara los módulos y ejecutara las funciones.

def depura(nif, ELIMINAMOS_CARACTERES):
    ''' Función que convierte una cadena de caracteres *EN MAYÚSCULAS*, y
        elimina el(los) caracter(es) especificado(s) en el 2º argumento.  '''

    nif = nif.upper() # - Pasamos minúsculas a mayúsculas.
    for elimino in ELIMINAMOS_CARACTERES:
        nif = nif.replace(elimino, "")
    return nif
