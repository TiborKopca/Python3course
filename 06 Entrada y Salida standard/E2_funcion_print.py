print('¿Qué sale de cruzar un mono con un pato?')

print('¡Un monopatín!')
print()
# Esta barra inversa indica que la letra que está a su derecha es un caracter de escape.
# Un caracter de escape te permite imprimir caracteres que son difíciles de introducir en el código fuente.
# En esta llamada a print() el caracter de escape es una comilla simple.
# El caracter de escape comilla simple está allí porque de otra manera Python pensaría que la
# comilla indica el final de la cadena. Pero esta comilla necesita formar parte de la cadena.
print('¿Porqué vuelan los pájaros pa\'l sur?')

print('¡Porque caminando tardarían muchísimo!')
print()

# La cadenas en Python no tienen que estar siempre entre comillas simples. También puedes ponerlas entre comilas dobles.
# Pero no puedes mezclar las comillas. 
print("¿En qué se parecen una familia, un bombero y un barco?")


# Salto de línea
print("No sé... \n ¿en qué se parecen?")

print('En que el bombero y el barco tienen casco.')

# Normalmente, print() añade un salto de línea al final de la cadena que imprime.
# Por esta razón, una función print() en blanco tan solo imprimirá una nueva línea.
# Pasando una cadena en blanco usando end, la función print() no añadirá un salto de linea al final de la cadena,
# en lugar de esto añadirá una cadena en blanco.  
print('¿Y la familia?', end='')
print(' -Bien, gracias.')
print()

# En las cadenas de comillas simples no necesitas escapar las comillas dobles,
# y en las cadenas de comillas dobles no necesitas escapar las comillas simples. 
print('Le pedí prestado el carro a Pedro pa\'ir al pueblo. El dijo, "Seguro."')
print()
print("Él dijo, \"No puedo creer que lo dejaste llevarse el carro pa'l pueblo\"")
print()

#Tabulador
print("Rojo \t Verde \t Azul \t Amarillo")
print("1 \t 2 \t 3 \t 4")
print('A \t B \t C \t D')
print()


print('Él se fue volando en un helicóptero verde\turquesa.')

# La "t" en "turquesa" fue vista como un caracter de escape debido a que estaba después de una barra inversa.
# El caracter de escape t simula la pulsación de la tecla TAB de tu teclado.

print('Él se fue volando en un helicóptero verde\\turquesa.')
