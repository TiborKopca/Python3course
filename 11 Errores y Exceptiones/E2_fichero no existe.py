#El fichero no existe
try:
    f = open("myarchivo.txt")
except FileNotFoundError:
    print("El fichero no existe")
else:
    print(f.read())
