#Importamos nuestro modulo contar_letras
import contar_letras as c



print('Se ejecuta como un modulo importado')
cadena = input("Escribe un texto por favor: ")
vocales = c.contarVocales(cadena)
consonantes = c.contarConsonantes(cadena)
print('El texto que has escrito', cadena,'tiene', vocales, 'vocales y', consonantes, 'consonantes')
