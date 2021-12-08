'''
Escribe un programa que lea una cadena escrita por teclado y compruebe si el primer y el último
carácter son iguales. Si son iguales, mostrará un mensaje con el número total de caracteres de la
cadena distintos a dicho carácter. En caso contrario, mostrará un mensaje con el número total de
caracteres de la cadena iguales al carácter inicial y al carácter final (sin incluirlos).
'''


#import module for clearing the screen
import os
#About
os.system('clear')#this is only for Linux, if this code fails in Windows, put it in comment
print('-------------------------------------------------------------------------------')
print("Programa para comprobar las cadenas de texto-si el primer y el último carácter son iguales.")
print('-------------------------------------------------------------------------------')

print('Escriba algun texto aqui:')
line = '-------------------------------------------------------------------------------'
cadena = input()
firstChar = cadena[0]
lastChar = cadena[len(cadena)-1]    #cadena[-1] is the same
# print(firstChar,"and",lastChar)

if cadena == '':    #The string is empty
    print('Error:No has entregano ningun texto. El programa termina.')
elif (firstChar == lastChar): #the first and the last character is the same
    sumaTotalchar = cadena.count(cadena[0])
    sumaTotalDistintos = len(cadena) - sumaTotalchar   #we can subtract whitespaces too  + cadena.count(' ')

    print(line)

    message = f'Suma de caracteres distintos a un primer caracter:{cadena[0]} es:{sumaTotalDistintos}.'
else:       #the first and last character are different
    # countFirstChar = cadena[1:].count(firstChar)
    countFirstChar = cadena.count(firstChar, 1,len(cadena))

    print(line)

    print(f'En el texto dado, el primer caracter {firstChar} se repite ademas {countFirstChar} veces en el texto.')
    countLastChar = cadena[:-1].count(lastChar)
    print(f'En el texto dado, el ultimo caracter {lastChar} se repite ademas {countLastChar} veces en el texto.')
    countCharactersTotal = countFirstChar + countLastChar
    message = f'Total caracters cual se repiten ademas de ser el primer o el ultimo son : {countCharactersTotal}.'
print(message)