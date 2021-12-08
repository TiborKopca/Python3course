#Diseñamos un programa para hallar el área de un  rectángulo.

#Pedimos el valor de la base
print('Valor de la base')
base = input()

#Lo convertimos a numero decimal
base = float(base)

#Pedimos el valor de la altura
print('Valor de la altura')
altura = input()

#Lo convertimos a numero decimal
altura = float(altura)

#Calculamos el área del rectangulo
area = base * altura

#Presentamos los resultados
print('El Area del rectangulo cuya base es', base, 'y cuya altura es', altura, 'tiene el valor de', area)
