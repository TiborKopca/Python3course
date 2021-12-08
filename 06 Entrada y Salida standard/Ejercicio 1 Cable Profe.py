#6) Sam Soprano instala cable coaxial para la Boston City Cable Company. Por cada instalación,
#hay una tarifa mínima por servicio de 25€ y una tarifa adicional de 2€ por cada metro de cable.
#Durante el mes de enero, Sam instaló un total de 2630 metros de cable en 27 lugares distintos.
#Desarrollar un programa informático para encontrar el beneficio generado por cualquier
#número de instalaciones, cualquier cantidad de cable, cualquier tarifa mínima y cualquier coste
#por unidad de cable.

#Solicitamos los datos
print("Ingrese la Tarifa de Servicio vigente.")
tarifaServicio = float(input())
print("Ingrese la Tarifa por metro de cable.")
costeCable = float(input())
print("Ingrese los metros de cable instalados.")
metrosCable = float(input())
print("Ingrese el numero de instalaciones realizadas.")
instalaciones = int(input())

#Calculamos
beneficio = (instalaciones * tarifaServicio) + (costeCable * metrosCable)

#Presentamos resultados
print("Se han realizado", instalaciones, "Instalaciones en las que se han usado", metrosCable, "metros de cable.\n Lo que ha supuesto un beneficio de", beneficio)   
