def calcular(importe, descuento):
    return importe - (importe * descuento / 100)

#Lista o Tupla
datos = [1500, 10]
print (calcular(*datos))    #1350.0

#Diccionario
datos = {"descuento": 10, "importe": 1500}
print(calcular(**datos))    #1350.0
