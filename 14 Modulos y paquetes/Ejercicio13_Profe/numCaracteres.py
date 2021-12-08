def numCaracteres(dni):
        '''Comprueba el numero de caracteres y devuelve true o false'''
        #Obtenemos el numero de caracteres
        numCaracteres = len(dni)
        #Hacemos la comprobacion
        if numCaracteres == 9 :
            return True
        else:
            return False
