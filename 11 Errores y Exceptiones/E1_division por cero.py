try:
    num1 = float(input("Introduce un número: ")) 
    num2 = float(input("Introduce otro número: ")) 
    c = num1/num2

except ZeroDivisionError: 
    print("No se puede dividir por cero")
else:
    print("El resultado es: ", c)
