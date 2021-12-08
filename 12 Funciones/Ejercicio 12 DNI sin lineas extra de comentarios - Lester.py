LONGITUD_NIF, DIVISOR_NIF = 9, 23
TUPLA_CONCORDANCIA = ("T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E")
def introduceNif():
    nif = input("Por favor, introduce el NIF:\n")
    return nif.upper().replace(" ", "").replace("-", "").replace("_", "").replace(".", "")
def longitud():
    if len(Nif) == LONGITUD_NIF:
        return "Longitud correcta."
    return f"Longitud incorrecta del NIF introducido ({Nif})."
def revisaDigitAlpha():
    for n in range(LONGITUD_NIF - 1):
        if Nif[n].isdigit() == False:
            return f"La posición {n + 1} del NIF {Nif} contiene el caracter '{Nif[n]}', pero debería ser algún número del 0 al 9."
    if Nif[LONGITUD_NIF - 1].isalpha() == False:
        return f"El último caracter del NIF {Nif} ha de ser una letra en vez de '{Nif[n + 1]}'."
    return "OkDigitAlpha."
def concordancia_DNI_LETRA():
    if TUPLA_CONCORDANCIA[int(Nif[0:LONGITUD_NIF - 1]) % DIVISOR_NIF] == Nif[LONGITUD_NIF - 1]:
        return f"El NIF: {Nif} tiene nuestra validación.\n"
    return f"El nº de NIF introducido: {Nif} no existe. Revísalo."
print("\nFalta introducir un NIF. Así que...")
Nif, MensajeErrorNif = "", ""
while MensajeErrorNif != f"El NIF: {Nif} tiene nuestra validación.\n":
    Nif = introduceNif() # ...y su retorno lo asigna a la variable global 'Nif'.
    print(f"\nNIF: {Nif} comprobando...")
    MensajeErrorNif = longitud() # Función que revisa la longitud del NIF.
    if MensajeErrorNif == "Longitud correcta.": # Si la longitud fue correcta,
        MensajeErrorNif = revisaDigitAlpha() # Función que revisa carácteres.
        if MensajeErrorNif == "OkDigitAlpha.": # Si los caracteres son correctos
            MensajeErrorNif = concordancia_DNI_LETRA() # Revisa si letra es Ok.
    print(MensajeErrorNif)