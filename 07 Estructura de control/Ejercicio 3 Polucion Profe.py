#Declaramos las variables
polucionEstacion = 0
polucionCentro = 0
polucionResidencial = 0
polucionTotal = 0

# Solicitamos los datos.
polucionEstacion = float(input('Polución Estación Tren '))
polucionCentro = float(input('Polución Centro Ciudad '))
polucionResidencial = float(input('Polución Barrio Residencial '))

#Calculamos la polución total
polucionTotal = round( ((polucionEstacion + polucionCentro + polucionResidencial) / 3),2)

#En función de la cantidad de polución mostramos un resultado u otro
if polucionTotal >= 50:
 print('¡PELIGRO! El nivel de polución es de', polucionTotal)
else:
 print('¡PERFECTO! El nivel de polución es de', polucionTotal)
