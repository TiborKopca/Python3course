#Bucle while controlado por centinela
#Declaramos las variables
tiempo_fallo = 0
suma_fallos = 0
media_fallos = 0
cuenta_fallos = 0

#Introducimos los datos
print('Ingrese el tiempo de fallo del circuito o pulse -1 para terminar')
tiempo_fallo = float(input())

#El centinela -1 sirve para finalizar la repetición 
while tiempo_fallo != -1 :

    #Calculamos la media
    #El centinela -1 no debe procesarse como un dato normal
    if tiempo_fallo != -1 :
        suma_fallos = suma_fallos +  tiempo_fallo
        cuenta_fallos = cuenta_fallos + 1

    #Introducimos los datos
    print('Ingrese el tiempo de fallo del circuito o pulse -1 para terminar')
    tiempo_fallo = float(input())
 

#Calcula la media
if cuenta_fallos > 0 :     
    media_fallos = round( suma_fallos /cuenta_fallos, 2)
    #Presentamos los resultados
    print('Se han introducido',cuenta_fallos, 'tiempos de media') 
    print('El tiempo medio de fallos es:', media_fallos)
else :
    print('No hay datos')
    





    
    
   

