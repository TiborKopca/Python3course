#Una variable booleana es una variable que sólo puede tomar dos posibles valores: True (verdadero) o False (falso).
#Para comprobar si un elemento se considera True o False,
#se puede convertir a su valor booleano mediante la función bool().

print(bool(0))      #False

print(bool(0.0))    #False

print(bool(""))     #False

print(bool(None))   #False

print(bool(25))     #True

print(bool(-9.5))   #True

print(bool("abc"))  #True

print('-----------------------------------------------------------------------')

#Los operadores lógicos son unas operaciones que trabajan con valores booleanos.

# and: "y" lógico. Este operador da como resultado True si y sólo si sus dos operandos son True:

print(True and True)    #True

print(True and False)   #False

print(False and True)   #False

print(False and False)  #False

print('-----------------------------------------------------------------------')

# or: "o" lógico. Este operador da como resultado True si algún operando es True:
print(True or True)     #True

print(True or False)    #True

print(False or True)    #True

print(False or False)   #False

print('-----------------------------------------------------------------------')

# not: negación. Este operador da como resultado True si y sólo si su argumento es False

print(not True)         #False
print(not False)        #True





