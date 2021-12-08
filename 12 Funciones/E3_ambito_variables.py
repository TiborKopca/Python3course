'''
Los lenguajes de programación limitan lo que se llama el alcance o el ámbito de las variables.
Es decir, que los lenguajes de programación permiten que una variable exista únicamente
en el interior de una subrutina y no afecte a otras variables de mismo nombre
situadas fuera de esa subrutina.
Como las subrutinas pueden contener a su vez subrutinas,
se suele hablar de niveles:
el nivel más alto sería el programa principal,
el siguiente nivel serían las subrutinas incluidas en el programa principal
y cada vez que hay una subrutina incluida dentro de otra estaríamos bajando un nivel.

En resumen:
Cada variable pertenece a un ámbito determinado: al programa principal o a una subrutina.
Las variables son completamente inaccesibles en los ámbitos superiores al ámbito al que pertenecen
'''

#Si no se han declarado como globales o no locales,
#las variables a las que se asigna valor en una función se consideran variables locales, es decir,
#sólo existen en la propia función, incluso cuando en el programa exista una variable con el mismo nombre.

def subrutina():
    a = 2 #Variable local
    print('Variable local: ',a) #2
    return

a = 5 #Variable global
subrutina()
print('Variable global: ',a)    #5
print('---------------------------------------------------------')

#Las variables locales sólo existen en la propia función
#y no son accesibles desde niveles superiores.

def subrutina():
    a = 2 #Variable local
    print('Variable local',a)   #2
    return

subrutina()
#print(a) #Esto dara error porque la variable "a" no existe para el programa, ya que se creó en la función.
print('---------------------------------------------------------')

'''
Las variables globales se pueden leer desde cualquier línea del
programa simplemente haciendo referencia a ellas a través de su
nombre. Pero no podemos modificar una variable global desde dentro
de una función.
Para modificarla es necesario utilizar el modificador global.
'''

contador = 10 #Variable global
def reiniciar_contador_fallido():
    contador = 0 #Variable local

def reiniciar_contador():
    global contador #Ahora podemos modificar la variable global
    contador = 0

print('Contador antes es: ' , contador)     #10
reiniciar_contador_fallido()                #no hace renicializacion de variable global

print('Contador después es: ', contador)    #10
print('---------------------------------------------------------')

print('Contador antes es: ' , contador)     #10
reiniciar_contador()                        #hace reinicializacion global

print('Contador después es: ', contador)    #0
print('---------------------------------------------------------')


