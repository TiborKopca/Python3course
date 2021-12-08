cadena1 = 'tengo una yama que Yama se llama'  # declara variable
print(cadena1)

longitud = len(cadena1)  # 32, devuelve longitud de la cadena
print('Longitud de la cadena ', longitud)

cuenta = cadena1.count('yama')  # 1, cuenta apariciones de 'yama'
print("cuenta apariciones de 'yama'", cuenta)

print("posición de yama",cadena1.find('yama'))  # 10, devuelve posición de búsqueda

cadena2 = cadena1.join('@@')  # inserta cadena1 entre caracteres
print(cadena2)  #@tengo una yama que Yama se llama@

cadena3 = cadena1.replace('yama','cabra',1) # busca/sustituye términos
print(cadena3)  #tengo una cabra que Yama se llama
print('----------------------------------------------')

numero = 3.14  # asigna número con decimales
cadena4 = str(numero)  # convierte número a cadena
print(cadena4)  #3.14
print('----------------------------------------------')

if cadena1.startswith("tengo"):
    # evalúa si comienza por “tengo”
    print('si comienza por “tengo”')

if cadena1.endswith("llama"):
    # evalúa si termina por “llama”
    print('si termina por “llama”')

if cadena1.find("llama") != -1:
    # evalúa si contiene “llama”
    print('si contiene “llama”')

print('----------------------------------------------')
cadena5 = 'Python'  # asigna una cadena a una variable
print(cadena5)
print(cadena5[0:4])  # muestra desde la posición 0 a 4: "Pyth"
print(cadena5[1])  # muestra la posición 1: "y"
print(cadena5[:3] + '-' + cadena5[3:])  # muestra "Pyt-hon"
print(cadena5[:-3])  # muestra todo menos las tres últimas: "Pyt"
print('----------------------------------------------')


# declara variable con cadena alfanumérica
cadena6 = "  abc;123  "
print(cadena6)

# suprime caracteres en blanco (y \t\n\r) por la derecha
print(cadena6.rstrip())  # "  abc;123"

# suprime caracteres en blanco (y \t\n\r) por la izquierda
print(cadena6.lstrip())  # "abc;123  "

# suprime caracteres en blanco (y \t\n\r) por derecha e izquierda
print(cadena6.strip())  # "abc;123"

# suprime caracteres del argumento por la derecha e izquierda
print(cadena6.strip("123456790; "))  # "abc"

print('----------------------------------------------')

cadena7 = "Mar"   # declara una variable
print(cadena7)
print(cadena7.upper())   # convierte a mayúsculas: "MAR"
print(cadena7.lower())   # convierte a minúsculas: "mar"
