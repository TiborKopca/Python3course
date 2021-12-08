# El Ministerio del Interior desea realizar una actualización del programa para la validación del
# DNI español.
# Hay que rehacer el programa del ejercicio 12 utilizando el paradigma de la programación
# Modular.
# Cada una de las funciones ira dentro de un módulo.
# Se desarrollará una función nueva que tome el numero introducido por el usuario y lo devuelva
# en MAYÚSCULAS con los espacios en blanco, los puntos, los guiones y los guiones bajos que el
# usuario introduzca junto con el número del DNI ELIMINADOS.
# El programa principal importara los módulos y ejecutara las funciones.


# INICIO

def main():

    from Ejercicio13_depuradorNIF import depura
    from Ejercicio13_longitudNIF import longitud
    from Ejercicio13_DigitAlphaNIF import revisaDigitAlpha
    from Ejercicio13_concordanciaNIF import concordancia_DNI_LETRA


    # VARIABLES CONSTANTES - según normas de NIFs válidos.
    ELIMINAMOS_CARACTERES = (" ", "-", "_", ".")
    LONGITUD_NIF, DIVISOR_NIF = 9, 23
    TUPLA_CONCORDANCIA = ("T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E")

    print("\nFalta introducir un NIF. Así que...", end="")

    # Variables que necesitamos inicializar ya (quiero usarlas en el 'while')...
    # Variable del Nif y variable del mensaje de error/validación de NIF (que
    # informará de cuál validación fracasó primera o si no fracasó ninguna).
    nif, MensajeErrorNif = "", ""

    # BLOQUE 'while' PARA INTRODUCIR (Y VALIDAR/REVISAR) EL NIF

    # 'Mientras el mensaje no sea éste...'
    while MensajeErrorNif != f"Tu NIF: {nif} tiene nuestra validación.\n":

        nif = input("\nIntroduce tu NIF:\n") # Pide el NIF

        # Ejecuta/llama a la Función que depura el NIF introducido
        nif = depura(nif, ELIMINAMOS_CARACTERES) # su retorno lo reasigna a nif.

        # Informa por pantalla que vamos a comprobar si ese NIF es falso.
        print(f"\nUn momento. Comprobamos si tu NIF {nif} es falso...")

        # Llamadas a Funciones que revisan la validez del NIF...

        # Llamada a la Función/revisión 'longitud()' y asignará su
        # resultado/retorno a la variable 'MensajeErrorNif'...
        MensajeErrorNif = longitud(nif, LONGITUD_NIF) # Revisa la longitud.
    
        # Si el resultado/retorno/texto de la anterior Función/revisión...
        if MensajeErrorNif == "Longitud correcta.": # Si longitud fue correcta,
        
            # entonces llama a la siguiente Función/revisión que REasignará su
            # resultado/retorno en esa misma variable 'MensajeErrorNif'...
            MensajeErrorNif = revisaDigitAlpha(nif, LONGITUD_NIF)
            # Revisa caracteres (que la primera parte sea un número, y el 
            # último caracter sea una letra.)

            # Si el resultado/texto retornado en la anterior Función/revisión...
            if MensajeErrorNif == "OkDigitAlpha.": # Si caracteres son correctos
            
                # entonces llama a siguiente Función/revisión que reasignará su
                # resultado/retorno como siempre en 'MensajeErrorNif'...
                MensajeErrorNif = concordancia_DNI_LETRA(nif, LONGITUD_NIF, DIVISOR_NIF, TUPLA_CONCORDANCIA)
                # Revisa si la Letra introducida por usuario es la reglamentaria
                # con el número de DNI que introdujo.
    
        # Muestra/informa el texto que se retornó en 'MensajeErrorNif'...
        print(MensajeErrorNif) # Y como es la última instrucción del bloque
        # 'while', ahora vuelve a la primera instrucción 'while' a comprobar si
        # este texto de MensajeErrorNif ha sido el de validación o no.

    # Si se ha salido del bloque 'while', es que el texto de 'MensajeErrorNif'
    # aprobaba nuestra validación (indicada en el 'while'). Y secuencialmente
    # (más abajo) ya no hay más instrucciones así que se acabó el programa aquí,
    # tras la instrucción anterior mostrando/informando tal validación.

if __name__ == '__main__':
    main()


# FIN
