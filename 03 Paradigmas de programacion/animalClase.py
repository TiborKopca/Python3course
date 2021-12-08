'''PROGRAMACIÓN ORIENTADA A OBJETOS'''

'''
Vamos a comparar entre la programación modular y la POO
para ello vamos a resolver un mismo problema utilizando
ambos paradigmas.

'''
#Los datos (propiedades o atributos) y las funciones (metodos) van juntos
#dentro de la clase


#Creamos la Clase Animal
class Animal:
    def __init__(self, energia):
        '''Constructor'''
        self.__energia = energia #Esto es un dato, la cantidad de energia

    def getEnergia(self):
        '''Metodoque nos devuelve la energia del animal''' 
        return self.__energia

    def sueño(self):
        '''Metodo que nos devuelve si el animal tiene sueño'''
        if self.getEnergia() < 10:
            sueño = 'Tiene sueño'
        else:
            sueño = 'No tiene sueño'
        return sueño

    

    
