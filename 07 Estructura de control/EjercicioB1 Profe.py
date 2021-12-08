#Pedimos los datos
print('Nombre y Apellidos:')
name = input()
print()
print('Nº Seguridad Social:')
numSeguridadSocial = input()
print()
print('Categoria (A,B,C):')
categoria = input()
print()
print('Sección (1,2,3,4):')
seccion = input()

suplemento = 240
#Si es de la categoria C
if categoria == 'C' :
    suplemento = 120
    sueldo = 650
    #Si es de la sección 1
    if seccion == '1':
        print('Dias trabajados:')
        dias = int(input())
        print()
        print('Ausencias no justificadas')
        ausencias = int(input())
        suplemento1 = dias * 0.5
        descuento = ausencias * 30
        suplemento =suplemento1 - descuento
    salario = sueldo + suplemento

#Si es de la categoria
elif categoria == 'B' :
    sueldo = 1000
    salario = sueldo + suplemento

#Si es de la categoria A
elif categoria == 'A' :
   sueldo = 1500
   salario = sueldo + suplemento

#Mostramos los resultados
print()
print('Nombre y Apellidos: ', name)
print('Nº Seguridad Social: ', numSeguridadSocial)
print('Categoria: ', categoria)
print('Sección: ', seccion)
print('Salario: ', salario, ' €')
print()




