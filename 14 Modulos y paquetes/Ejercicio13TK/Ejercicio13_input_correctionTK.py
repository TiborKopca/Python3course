def stripData(stringDNI):
    '''Funcion corrige el numero introducido por el usuario y lo devuelva en MAYÚSCULAS con los espacios en blanco, los puntos, los guiones y los guiones bajos'''
    #TIP - atribute in the function MUST be parsed to STRING to make OPERATIONS on it..
    stringDNI = str(stringDNI).replace(" ", "").replace('-','').replace('_','').replace('.','').strip().upper()
    return stringDNI

