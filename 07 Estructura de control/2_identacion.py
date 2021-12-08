#Identación
#En un lenguaje informático, la identación es lo que la sangría al
#lenguaje humano escrito (a nivel formal).
#Los espacios al principio de una línea (el sangrado) son significativos
#porque indican un nivel de agrupamiento.
#Otros lenguajes utilizan un caracter, las llaves { }, para delimitar agrupamientos
#Una identación de 4 (cuatro) espacios en blanco, indicará que las
#instrucciones identadas, forman parte de una misma estructura de control.

#Escribe muchas líneas de salida

print('Escribe muchas líneas de salida')

a=0
for (i) in range (5):
  a=a+i
  print (a)


#El print del prime código forma parte del bloque del for.
#Así pues se ejecuta en cada iteración, y por eso se escriben
#múltiples líneas de salida.


print('--------------------------')

#Escribe  solo una línea de salida
print('Escribe  solo una línea de salida')

a=0
for (i) in range (10):
  a=a+i
print (a) 


#En el segundo código, el print esta fuera del bloque
#y por lo tanto se ejecuta solo una vez.
