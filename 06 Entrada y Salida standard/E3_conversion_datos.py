# De forma predeterminada, la función input() convierte la entrada en
# una cadena, aunque escribamos un número.
# Para poder usar un tipo de dato diferente a una cadena en nuestro código
# es necesario hacer una conversión explicita (casting).

edad = int(input('Teclear edad: ')) # entrada de entero
peso = float(input('Teclear peso: ')) # entrada de flotante
nombre = input('Teclear nombre: ') # entrada de cadena
print(nombre, edad, 'años', peso, 'kg') # muestra datos
