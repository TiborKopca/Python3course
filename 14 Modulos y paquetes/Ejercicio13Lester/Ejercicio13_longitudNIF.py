def longitud(nif, LONGITUD_NIF):
    ''' Esta Función revisa la longitud del NIF.'''
    
    # Si la longitud de la variable global 'nif' es igual a la LONGITUD que ha
    # de tener un NIF:
    if len(nif) == LONGITUD_NIF:
        # Esta revisión puede retornar con un texto: "Longitud correcta." que
        # será asignado a la variable global 'MensajeErrorNif' porque se llamó a
        # esta función con la instrucción "MensajeErrorNif = longitud()".
        return "Longitud correcta."
    
    # Si no se ha cumplido lo anterior, entonces esta revisión retorna asignando
    # (a dicha variable con la que se llamó a esta Función) el texto...
    return f"Longitud incorrecta del NIF introducido ({nif})."
