'''El módulo datetime va a permitirte manipular fechas de forma sencilla.'''

import datetime

#creamos un objeto de tipo Datetime
#pasándole como parámetros el año, el mes, el día, la hora, los minutos,
#los segundos y los microsegundos.

fecha = datetime.datetime(2016,2,21,14,00,00,000)
print(fecha)                                        #2016-02-21 14:00:00
print("Año: ",fecha.year)                           #Año:  2016
print("Mes: ",fecha.month)                          #Mes:  2
print("Día: ",fecha.day)                            #Día:  21
print("Hora: ",fecha.hour)                          #Día:  21
print("Minutos: ",fecha.minute)                     #0
print("Segundos: ",fecha.second)                    #0
print("Microsegundos: ",fecha.microsecond)          #0

print()
print()

#creamos un objeto de tipo Datetime conla fecha y la hora del sistema
fecha =datetime.datetime.now()                      #2021-12-02 14:40:28.500546
print(fecha)
print("Año: ",fecha.year)
print("Mes: ",fecha.month)
print("Día: ",fecha.day)
print("Hora: ",fecha.hour)
print("Minutos: ",fecha.minute)
print("Segundos: ",fecha.second)
print("Microsegundos: ",fecha.microsecond)

print()
print()

#Función que retorna el día de hoy.
fecha = datetime.date.today()
print(fecha)                    #2021-12-02
print("Año: ",fecha.year)       #Año:  2021
print("Mes: ",fecha.month)      #Mes:  12
print("Día: ",fecha.day)        #Día:  2

print()
print()

# Calcula la diferencia entre dos datetime.

fin = datetime.datetime.now()
inicio = datetime.datetime(2016,2,21,14,00,00,000)
print("Resta de fechas:")
print("1.- ", fin)                      #1.-  2021-12-02 14:40:28.500989
print("2.- ", inicio)                   #2.-  2016-02-21 14:00:00
resultado = fin - inicio
print("Resultado: ",resultado)          #Resultado:  2111 days, 0:40:28.500989

# Calcula la diferencia entre dos date
fin = datetime.datetime.now()
inicio = datetime.datetime(2016,2,21,14,00,00,000)
print("Resta de fechas:")
print("1.- ", fin)                      #1.-  2021-12-02 14:40:28.501057
print("2.- ", inicio)                   #2.-  2016-02-21 14:00:00
resultado = fin - inicio
print("Resultado: ",resultado)          #Resultado:  2111 days, 0:40:28.501057



