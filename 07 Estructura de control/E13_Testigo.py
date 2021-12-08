#Testigo

'''Se entiende por testigo una variable que indica simplemente si una condición se ha cumplido o no.
Es un caso particular de contador,
pero se suele hacer con variables lógicas en vez de numéricas
(en este caso, la variable que hace de testigo es la variable encontrado)'''

'''En cada iteración, el programa comprueba si i es múltiplo de 2.
El testigo se modifica la primera vez que la variable de control i es múltiplo de 2.
El testigo no cambia una vez ha cambiado.
Antes del bucle se debe dar un valor inicial al testigo (en este caso, False)'''

print("Comienzo")
encontrado = False
for i in range(1, 6):
    if i % 2 == 0:
        encontrado = True
if encontrado:
    print(f"Entre 1 y 5 hay al menos un múltiplo de 2.")
else:
    print(f"Entre 1 y 5 no hay ningún múltiplo de 2.")
