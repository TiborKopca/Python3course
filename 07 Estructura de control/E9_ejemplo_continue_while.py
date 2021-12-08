'''
El uso de continue al igual que el ya visto break, nos permite modificar
el comportamiento de los bucles while y for.
continue se salta todo el código restante en la
iteración actual y vuelve al principio en el caso de que aún queden
iteraciones por completar.
'''
suma = 0
i = 0
while i <= 10 :
   i = i+1
   suma = suma + i
print ("La suma del 1 al 10 inclusive es: ", suma)

#----------------------------------------------------------------------------------------------

suma = 0
i = 0
while i <= 10 :
   i = i+1
   print('i =', i)
   #Si es multiplo de cuatro vuelve al principio del buckle
   if i % 4 == 0:
        continue

   suma = suma + i
   print('suma = ',suma)
print("La suma del 1 al 10 inclusive salvo los múltiplos de 4 es:", suma)
