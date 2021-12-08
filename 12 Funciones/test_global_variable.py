x = 5

def suma():
    global x
    x += 5
    print('en funcion',x)
    return x

print('valor es ',x)
suma()
print('despues y afuera de funcion',x)
