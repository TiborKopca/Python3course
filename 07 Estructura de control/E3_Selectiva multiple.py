#Selectivas múltiples

'''En una estructura if ... elif .. else cuando se cumple una de las comparaciones Python ya no evalúa las siguientes condiciones.
En este caso, si el programa tiene que comprobar la segunda comparación (la del elif), es porque no se ha cumplido la primera (la del if).'''

edad = int(input("¿Cuántos años tiene? "))
if edad < 0:
    print("No se puede tener una edad negativa")
elif edad < 18:
    print("Es usted menor de edad")
else:
    print("Es usted mayor de edad")


'''Pero hay que tener cuidado, porque si los casos del programa anterior se ordenan al revés manteniendo las condiciones,
el programa no funcionaría como se espera, puesto que al escribir un valor negativo mostraría el mensaje "Es usted menor de edad".'''

# Este programa no funciona correctamente
edad = int(input("¿Cuántos años tiene? "))
if edad < 18:
    print("Es usted menor de edad")
elif edad < 0:
    print("No se puede tener una edad negativa")
else:
    print("Es usted mayor de edad")
