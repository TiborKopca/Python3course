'''
6) Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un descuento
del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del
día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le
hace por no ser fresca y el coste final total
'''
#import module for clearing the screen
import os
#About
os.system('clear')#this is only for Linux, if this code fails in Windows, put it in comment
print('-------------------------------------------------------------------------------')
print("Programa para hacer calculaciones para vendedores del pan.")
print('-------------------------------------------------------------------------------')


PRECIO_PAN_FRESCO = 3.49
DESCUENTO = 60              #in %
PRECIO_PAN_ANEJO = round(PRECIO_PAN_FRESCO - (PRECIO_PAN_FRESCO * DESCUENTO / 100) ,2) #rounded to 2 digits
barasAnejoVendidas = int(input('Introduzca el numero de barras de pan del antedia(tipo anejo) por favor:'))

if barasAnejoVendidas <= 0:
    print('Lectura erronea, no se puede calcular con datos introducidos.')
else:
    precioHabitual = round(barasAnejoVendidas * PRECIO_PAN_FRESCO,2)
    precioConDescuento = round(barasAnejoVendidas * PRECIO_PAN_ANEJO,2)
    diferencia = round(precioHabitual - precioConDescuento,2)

    print(f'Precio habitual seria(si fuesen frescas):{precioHabitual} Eur')
    print(f'Descuento por no ser frescos:{diferencia} Eur')
    print('-------------------------------------------------------------------------------')
    print(f'Coste final con despues descuento: {precioConDescuento} Eur')

    print('Bon profit!')