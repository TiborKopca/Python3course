def subrutina():
    a = 2
    print(a)
    return
subrutina() #2
print(a) # NameError: name 'a' is not defined

contador = 10
def reiniciar_contador():
    global contador
    contador = 0
print(f'Contador antes es {contador}')  #Contador antes es 10
reiniciar_contador()
print(f'Contador después es {contador}') #Contador después es 0