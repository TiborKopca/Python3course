'''Modulo para contar las vocales y consonantes de una cadena'''

#Importamos el modulo re
import re


#Creamos la función
def contarVocales(texto):
    '''Calcula el total de vocales que tiene un texto'''
    totalVocales = len(re.findall("[aeiouáéíóú]",texto, re.IGNORECASE))
    return totalVocales

#Creamos la función
def contarConsonantes(texto):
    '''Calcula el total de consonantes que tiene un texto'''
    totalConsonantes = len(re.findall("[bcdfghjklmnñpqrstvwxyz]",texto, re.IGNORECASE))
    return totalConsonantes


#Esta función solo se ejecutara cuando se ejecute como script
def main():
    print('Se ejecuta como script')
    cadena = input("Escribe un texto: ")
    vocales = contarVocales(cadena)
    consonantes = contarConsonantes(cadena)
    print('El texto', cadena,'tiene', vocales, 'vocales y', consonantes, 'consonantes')

if __name__ == "__main__":
    main()
                       
                       
