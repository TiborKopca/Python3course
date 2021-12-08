def prepararDatos(mydato):
    ''' Elimina los espacios,los puntos,los guiones yos guiones bajos que el usuario introduzca junto con el número
    Tambien pone el numero en mayuscula'''
    #Eliminamos los espacios que el usuario introduzca junto con el número del DNI.
    mydato = mydato.replace('  ','')

    #Eliminamos los puntos que el usuario introduzca junto con el número del DNI.
    mydato = mydato.replace('.','')
    
    #Eliminamos los guiones que el usuario introduzca junto con el número del DNI.
    mydato = mydato.replace('-','')

    #Eliminamos los guiones bajos que el usuario introduzca junto con el número del DNI.
    mydato = mydato.replace('_','')

    #Lo ponemos todo en mayusculas
    mydato = mydato.upper()

    #Devolvemos el resultado
    return mydato
