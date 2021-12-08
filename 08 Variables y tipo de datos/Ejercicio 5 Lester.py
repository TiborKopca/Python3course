#!/usr/bin/env python
#Tema 8 ejercicio 5
# Escribe un programa que lea una cadena escrita por teclado y compruebe si el primer y el último
#carácter son iguales. Si son iguales, mostrará un mensaje con el número total de caracteres de la
#cadena distintos a dicho carácter. En caso contrario, mostrará un mensaje con el número total de
#caracteres de la cadena iguales al carácter inicial y al carácter final (sin incluirlos).
cadena = input("Introduzca una cadena de texto, por favor:")
#variable para contar los caracteres iguales o diferentes, segun el caso
contador = 0
#el contador del primer caracter si es diferente del ultimo
contaPrimera = 0
#el contador del ultimo caracter si es diferente del primero
contaUltima = 0
#Si el primer y el utlimo caracter son iguales cuenta los  caracteres que no les son iguales
#Si son diferentes cuenta los iguales al primero y al ultimo
if cadena[0] == cadena[-1]:
    for i in cadena:
        if i != cadena[0]:
            contador += 1
    print(f"La cadena empieza y termina con el caracter \'{cadena[0]}\'.")
    print(f"En la cadena \'{cadena}\' hay {len(cadena)} caracteres y en la cadena hay {contador} caracteres distintos de \'{cadena[0]}\'.")
else:
    for i in cadena:
        if i == cadena[0]:
            contaPrimera += 1
    for j in cadena:
        if j == cadena[-1]:
            contaUltima += 1
    contador = contaPrimera + contaUltima
    print(f"En la cadena \'{cadena}\' hay {contador -2} caracteres iguales a \'{cadena[0]}\' y \'{cadena[-1]}\'.")
            
    