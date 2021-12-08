# El Ministerio del Interior nos ha contratado para realizar un programa para la
# validación del DNI español.
# El programa tendrá las siguientes especificaciones:
# ✓ El usuario introducirá el número de su DNI con la letra en una sola entrada
# (11111111A)
# ✓ Se comprobará si el número de caracteres introducido es el correcto, sabiendo
# que el DNI tiene 9 caracteres
# ✓ Se comprobará que la letra este dentro del rango de letras usadas, sabiendo que
# las letras usadas son: T, R, W, A, G, M, Y, F, P, D, X, B, N, J, Z, S, Q, V, H, L, C, K, E.
# ✓ Se comprobará que la letra corresponde al número del DNI. Sabiendo que La
# letra se obtiene: calculando el resto de la división del número del DNI por 23. A
# cada resultado le corresponde una letra: 0=T; 1=R; 2=W; 3=A; 4=G; 5=M; 6=Y;
# 7=F; 8=P; 9=D; 10=X; 11=B; 12=N; 13=J; 14=Z; 15=S; 16=Q; 17=V; 18=H; 19=L;
# 20=C; 21=K; 22=E.
# El director del proyecto nos indica que el programa tiene que resolverse usando el
# paradigma de la programación modular y nos sugiere utilizar tres funciones: una para
# comprobar la cantidad de caracteres, otra para comprobar si la letra esta dentro del
# rango y la ultima para comprobar si la letra se corresponde al número del DNI.
# La validación será progresiva, de lo mas sencillo a lo mas complicado. En el momento en
# que falle una validación se avisara al usuario que el número introducido es incorrecto.



# INICIO


# Variables CONSTANTES (todos sus nombres con mayúsculas).

# La longitud del NIF actualmente es de 9 caracteres.
# Y dividimos entre 23 para validar la letra del NIF.
LONGITUD_NIF, DIVISOR_NIF = 9, 23
# También es una constante la variable (tupla)...
TUPLA_CONCORDANCIA = ("T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E")



# FUNCIONES-SUBRUTINAS

def introduceNif():
    ''' Esta función pide al usuario que introduzca el nº de NIF y lo depura.'''
    
    # El NIF que se introduzca se guarda en esta variable local ('nif').
    nif = input("Por favor, introduce el NIF:\n")
        
    # Saldremos de la función retornando como resultado la depuración de la
    # variable indicada localmente ('nif'). La depuración será:
    # - Pasamos minúsculas a mayúsculas.
    # - Reemplazamos: espacios, guiones, guiones bajos y puntos, por nada: "".
    #   Es decir: que estos 'reemplazos' vienen a significar 'eliminaciones'.
    return nif.upper().replace(" ", "").replace("-", "").replace("_", "").replace(".", "")
    # Este retorno se asignará a nuestra variable global 'Nif' porque se llamó
    # a esta Función asignando la variable (global) "Nif = introduceNif()".


def longitud():
    ''' Esta Función revisa la longitud del NIF introducido.'''
    
    # Si la longitud de la variable global 'nif' es igual a la LONGITUD que ha
    # de tener un NIF:
    if len(Nif) == LONGITUD_NIF:
        # Esta revisión puede retornar con un texto: "Longitud correcta." que
        # será asignado a la variable global 'MensajeErrorNif' porque se llamó a
        # esta función con la instrucción "MensajeErrorNif = longitud()".
        return "Longitud correcta."
    
    # Si no se ha cumplido lo anterior, entonces esta revisión retorna asignando
    # (a dicha variable con la que se llamó a esta Función) el texto...
    return f"Longitud incorrecta del NIF introducido ({Nif})."


def revisaDigitAlpha():
    ''' Esta Función revisa que todos los caracteres sean dígitos, y que el
    último caracter sea una letra.'''

    # Revisa uno a uno toda la longitud del NIF (excepto el último carácter, es
    # decir: hasta el penúltimo carácter), que cada caracter sean un dígito.
    for n in range(LONGITUD_NIF - 1):

        # Si el caracter de la posición 'n' no es un dígito (caracter numérico).
        if Nif[n].isdigit() == False:
            # entonces retorna con este texto de error...
            return f"La posición {n + 1} del NIF {Nif} contiene el caracter '{Nif[n]}', pero debería ser algún número del 0 al 9."
        # De lo contrario (si sí es un dígito) entonces comprueba el siguiente
        # caracter (posición) del nif ('for n in...') y así hasta el penúltimo
        # caracter de la longitud del nif: 'range(LONGITUD_NIF - 1)'

    # Si completó el anterior 'for n in...' es que todos fueron dígitos (ok), y
    # entonces ahora revisa solo el último caracter para saber si éste es, o no,
    # alguna letra.
    # Si el último caracter no es 'alpha' (si no es una letra)...
    if Nif[LONGITUD_NIF - 1].isalpha() == False:
        # entonces retorna con este texto de error...
        return f"El último caracter del NIF {Nif} ha de ser una letra en vez de '{Nif[n + 1]}'."
    
    # Si no ha retornado antes, entonces es que el último carácter era una Letra
    # y entonces esta revisión retorna asignando (a la variable global con la
    # que se asignó la llamada a esta Función) el texto...
    return "OkDigitAlpha."


def concordancia_DNI_LETRA():
    ''' Esta Función revisa que la letra correspondiente al resto (de la
    división del DNI entre 23) coincida con la letra de ese último carácter del
    NIF introducido.'''

    # Busca la posición/elemento de la tupla (variable constante
    # TUPLA_CONCORDANCIA) según el 'resto' de la división del DNI por 23, para
    # obtener el valor de dicho elemento, y compararlo con el valor del último
    # caracter del Nif introducido. Deben coincidir para estar Ok.
    if TUPLA_CONCORDANCIA[int(Nif[0:LONGITUD_NIF - 1]) % DIVISOR_NIF] == Nif[LONGITUD_NIF - 1]:
        # Si coincidieron, entonces esta Función(revisión) retorna asignando (a
        # la variable global ('MensajeErrorNif') con la que se asignó la llamada
        # a esta Función) el texto...
        return f"El NIF: {Nif} tiene nuestra validación.\n"

    # Si no ha retornado con el anterior texto (si no se ha cumplido, por tanto,
    # esa condición), así que esta revisión retorna ahora asignando (a dicho
    # valor de siempre: 'MensajeErrorNif') el texto...
    return f"El nº de NIF introducido: {Nif} no existe. Revísalo."



# ******** PROGRAMA *********

print("\nFalta introducir un NIF. Así que...")

# Variables que necesitamos inicializar ya (para usarlas en el 'while')...

# Variable del Nif y variable del mensaje de error/validación de NIF (que
# informará de cuál validación fracasó primera o si no fracasó ninguna).
Nif, MensajeErrorNif = "", ""


# BLOQUE 'while' PARA INTRODUCIR (Y VALIDAR/REVISAR) EL NIF

# 'Mientras el mensaje no sea éste...'
while MensajeErrorNif != f"El NIF: {Nif} tiene nuestra validación.\n":

    # Ejecuta/llama a la Función 'introduceNif()'...
    Nif = introduceNif() # ...y su retorno lo asigna a la variable global 'Nif'.

    # Informa por pantalla que vamos a hacer algunas comprobaciones al Nif.
    print(f"\nNIF: {Nif} comprobando...")

    # Llamadas a Funciones que revisan la validez del Nif introducido...

    # Llamada a la Función/revisión 'longitud()' y asignará su resultado/retorno
    # a la variable global 'MensajeErrorNif'...
    MensajeErrorNif = longitud() # Función que revisa la longitud del Nif.
    
    # Si el resultado/retorno/texto de la anterior Función/revisión...
    if MensajeErrorNif == "Longitud correcta.": # Si la longitud fue correcta,
        
        # entonces llama a la siguiente Función/revisión que REasignará su
        # resultado/retorno en esa misma variable global 'MensajeErrorNif'...
        MensajeErrorNif = revisaDigitAlpha() # Función que revisa carácteres.

        # Si el resultado/texto retornado en la anterior Función/revisión...
        if MensajeErrorNif == "OkDigitAlpha.": # Si los caracteres son correctos
            
            # entonces llama a la siguiente Función/revisión que reasignará su
            # resultado/retorno como siempre un texto y en 'MensajeErrorNif'...
            MensajeErrorNif = concordancia_DNI_LETRA() # Revisa si letra es Ok.
    
    # Muestra/informa el texto retornado a 'MensajeErrorNif'...
    print(MensajeErrorNif) # Y como es la última instrucción del bloque 'while',
    # ahora vuelve a la primera instrucción 'while' a comprobar si este texto de
    # MensajeErrorNif ha sido el de validación o no.

# Si se ha salido del bloque 'while', es que el texto de 'MensajeErrorNif'
# aprobaba nuestra validación (indicada en el 'while'). Y secuencialmente (más
# abajo) ya no hay más instrucciones así que se acabó el programa aquí, tras la
# instrucción anterior mostrando/informando tal validación.

# Total: 31 líneas de código, si es que las he contado bien.

# FIN