#About
print('Calcula salario segun sueldo y horas dadas.')
#Input data + declaration of data
nombre = str(input('Escriba su nombre:'))
numeroSocial = str(input('Escriba tu numero social:'))
sueldoBase = float(input('Dame tu sueldo:'))
horasTrabajadoras = int(input('Cuantas horas has trabajado?:'))

#Calculations
salarioTotal = float(sueldoBase * horasTrabajadoras)

#Output
print("Don",nombre, "con numero de la SS:",numeroSocial,"ha trabajado"\
      ,horasTrabajadoras,"horas, cobrandolas a",sueldoBase,"€ la hora.")
print("Su salario es de",salarioTotal,"Euros.")

#PSEUDOCODIGO
#INICIO Calculacion de salario
#ESCRIBIR Informacion que haga el programa
#LEER String Nombre
#LEER Numero Seguridad Social
#LEER Numero Sueldo base
#LEER Numero horas Trabajadoras
#CALCULAR
#ESCRIBIR Resumen y el resultado
#FIN