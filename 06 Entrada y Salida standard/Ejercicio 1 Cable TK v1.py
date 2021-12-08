"""
Sam Soprano instala cable coaxial para la Boston City Cable Company. Por cada instalación, hay
una tarifa mínima por servicio de 25€ y una tarifa adicional de 2€ por cada metro de cable. Durante
el mes de enero, Sam instaló un total de 2630 metros de cable en 27 lugares distintos. Desarrollar un
programa informático para encontrar el beneficio generado por cualquier número de instalaciones,
cualquier cantidad de cable, cualquier tarifa mínima y cualquier coste por unidad de cable.
Presentar la siguiente documentación:
➔ ALGORITMO EN SEUDOCÓDIGO.
➔ ALGORITMO EN DIAGRAMA DE FLUJO.
➔ PROGRAMA INFORMÁTICO EN PYTHON
"""

#PSEUDOCODIGO
#INICIO Beneficio generado de Instalaciones cable
#ESCRIBIR Informacion que haga el programa
#ESCRIBIR "Escriba numero de instalaciones hechas:"
#LEER Numero instalaciones
#ESCRIBIR "Escriba metros cables consumidos/instalados en metros:"
#LEER Numero candidad cable
#ESCRIBIR "Escriba el coste del cable por metro en Euros:"
#LEER Numero coste cable
#ESCRIBIR "Escriba tarifa minima por servicio en Euros:"
#LEER Numero tarifa instalacion
#CALCULAR (nIstalaciones*nTarifa)+(nCandidadCable*nCosteCable)
#ESCRIBIR Resumen y el resultado
#FIN

#About
print('Programa nos da el beneficio generado por instalaciones,candidad de cable, tarifa y coste de cable.')
#Input Data from the user
nIstalaciones = int(input('Escriba numero de instalaciones hechas:'))
nCandidadCable = float(input('Escriba metros cables consumidos/instalados en metros:'))
nCosteCable = float(input('Escriba el coste del cable por metro en Euros:'))
nTarifa = float(input('Escriba tarifa minima por servicio en Euros:'))
#Calculations
formula = (nIstalaciones*nTarifa)+(nCandidadCable*nCosteCable)
#Output
print('Resumen:\n'\
      'Instalaciones hechas:',nIstalaciones,'\n'\
      'Cable consumido en total(metros):',nCandidadCable,'\n'\
      'Coste de cable por metro(euros):',nCosteCable,'\n'\
      'Tarifa por servicio base(euros):',nTarifa,'\n'\
      'Beneficio generado:',formula,'Euros')



