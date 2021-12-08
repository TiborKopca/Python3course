def desguazar(dividendo, divisor):
    cociente = dividendo//divisor
    resto = dividendo%divisor
    return cociente,resto
x,y = desguazar(14,4)
print(x,y)      #Devuelve x=3, y=2