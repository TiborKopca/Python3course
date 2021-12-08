
print("CÁLCULO DEL ÍNDICE DE MASA CORPORAL (IMC)")
print()
peso = float(input("¿Cuánto pesa en Kg? "))
altura = float(input("¿Cuánto mide en metros? "))

imc = round((peso / altura ** 2),1)

if imc < 18.5 :
    mensaje = 'Peso inferior al norma'
elif imc >= 18.5 and imc <= 24.9 :
    mensaje = 'Peso Norma'
elif imc >= 25 and imc <= 29.9 :
    mensaje ='Peso superior al norma'
elif imc > 30 :
    mensaje = 'OBESIDAD'

print()
print('Su imc es: ',imc)
print()
print(mensaje)


