#!/usr/bin/env python
#Generador de DNI valido
#Se genera un numero de 8 digitos, se divide este numero por 23 y el resto de la division
#se usa para elegir la letra correspondiente de entre las letras validas
#Luego se muestra por pantalla el conjunto del numero y la letra
import random
longitud = 0
letrasValidas = ('T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E')
while longitud != 8:
    numero = random.randint(0, 99999999)
    numberString = str(numero)
    longitud = len(numberString)
    resto = numero % 23
    letra = letrasValidas[resto]
print(f"DNI valido: {numero}{letra}")
