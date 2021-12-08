#Una vez se ha definido una variable, se puede utilizar para hacer cálculos o para definir nuevas variables,
#como muestran los siguientes ejemplos:

a = 2
print(a + 3)

horas = 5
minutos = 60 * horas
segundos = 60 * minutos
print(segundos)

#Se puede redefinir una variable a partir de su propio valor. Por ejemplo

a = 10
a = a + 5
print(a)

'''
Esto es posible porque el símbolo de igualdad significa siempre asignación.
Lo que hace Python es calcular la expresión situada a la derecha de la igualdad
y después guardar el resultado en la variable situada a la izquierda de la igualdad.
En el ejemplo, Python coge el valor almacenado en la variable a (10), le suma 5, y el resultado (15)
lo guarda en la misma variable a.

Es importante tener presente que las igualdades son siempre asignaciones, nunca ecuaciones.
En el ejemplo, la expresión a = a + 5 no tendría mucho sentido como ecuación (no tendría solución),
pero como asignación lo que hace es aumentar en 5 el valor de la variable a.
'''

#Cuando se modifica una variable, el valor anterior se pierde y no se puede recuperar.

a = 5
a = 2
print(a)

#salvo si hay otra variable que conserva el valor anterior).
a = 5
b= a
a = 2
print(b)
print(a)
