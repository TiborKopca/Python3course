#Este programa puede incluir un bucle que se ejecute tantas veces como palabras tiene la lista.
#En cada iteración del bucle, se pide un valor y se añade a la lista.

numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)

'''
Para contar los elementos, este programa puede incluir
un bucle que recorra la lista una vez creada.
Puesto que no se van a modificar los valores de la lista,
la lista se puede recorrer directamente (for i in lista).
En cada iteración del bucle, se compara el valor de la lista
con el valor buscado y si coinciden, se aumenta el valor de un contador.
'''

buscar = input("Dígame la palabra a buscar: ")
contador = 0
for i in lista:
    if i == buscar:
        contador += 1;
if contador == 0:
    print("La palabra '" + buscar + "' no aparece en la lista.")
elif contador == 1:
    print("La palabra '" + buscar + "' aparece una vez en la lista.")
else:
    print("La palabra '" + buscar + "' aparece", contador, "veces en la lista.")
