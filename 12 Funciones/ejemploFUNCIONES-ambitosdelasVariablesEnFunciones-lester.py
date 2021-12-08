def mayor(a, b):
    """Esta función devuelve el mayor de los valores"""
    if a > b: #fijase que esta función usa las variables a/b, que al estar en una función son "variables LOCALES"
        return a
    return b

print("hola mundo")

a, b = 15, 12 # Aquí las variables a/b son GLOBALES
c, d = 22, 33 # Estas también
print (a, b, c, d)
resul = mayor(a, b)

print(mayor(c, d))
print("a=", a, "   b=", b, "   c=", c, "   d=", d, "   y el mayor es", resul)
print()
help(mayor)
print(mayor.__doc__)
