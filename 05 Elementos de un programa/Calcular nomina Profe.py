#Declaramos las variables.
nombre = ""
numeroSocial = ""
sueldoBase = 0
horasTrabajadas = 0
salarioTotal = 0

#Pedimos los datos.
print('Nombre y Apellidos')
nombre = input()
print('Número Seguridad Social')
numeroSocial = input()
print('¿Cuánto cobras por hora trabajada?')
sueldoBase = float(input())
print('¿Cuántas horas has trabajado este mes?')
horasTrabajadas = float(input())

#Calculamos el salario
salarioTotal =sueldoBase * horasTrabajadas

#Presentamos los resultados
print('Don', nombre, 'con número de la SS', numeroSocial, 'ha trabajado', horasTrabajadas, 'cobrándolas a', sueldoBase, '€ la hora.')
print('Su salario es de', salarioTotal, 'Euros.')
