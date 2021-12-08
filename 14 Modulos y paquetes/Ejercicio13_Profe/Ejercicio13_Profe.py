#Importamos los modulos
import prepararDatos as datos
import numCaracteres as numc
import esLetra as letra
import validarLetra as validar





if __name__ == "__main__":

    #Pedimos el numero de DNI    
    print('Introduzca su numero de DNI:')
    mydni = input()

    resultado = datos.prepararDatos(mydni)




    #Comprobamos el numero de caracteres
    if numc.numCaracteres(resultado):
        #Comprobamos si la letra este dentro del rango de letras usadas por el DNI
        if letra.esLetra(resultado):
            #Comprobamos si la letra es correcta
            if validar.validarLetra(resultado):
                print('Su DNI es correcto') 
            else:
                print('La letra de su DNI no es la que le corresponde')

        else:
           print('La letra introducida no es ninguna de las usadas en los DNI')

    else:
       print('El numero de caracteres introducido no es correcto') 
        
        
            
            
        
    
