'''
El uso de continue al igual que el ya visto break, nos permite modificar
el comportamiento de los bucles while y for.
continue se salta todo el código restante en la
iteración actual y vuelve al principio en el caso de que aún queden
iteraciones por completar.
'''
suma = 0
for i in range(101):
    if i == 3 or i == 19 or i == 32:
        continue
    suma = suma + i
print ("La suma con continue (sin sumar 3, 19 y 32) ha sido: ", suma)

print('--------------------------------------------------------------------')

suma = 0
for i in range(101):
    suma = suma + i
print ("La suma sin continue (sumando todos) ha sido: ", suma)
