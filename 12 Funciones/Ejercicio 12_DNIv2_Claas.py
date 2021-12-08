#!/usr/bin/env python
#Tema 12, ejercicio 12: El  Ministerio  del  Interior  nos  ha  contratado  para  realizar
#un  programa  para  la validación del DNI español.El programa tendrá las siguientes especificaciones:
#✓El  usuario  introducirá  el  número  de  su  DNI  con  la  letra  en  una  sola  entrada(12345678A)
#✓Se comprobará si el número de caracteres introducido es el correcto, sabiendo que el DNI tiene 9 caracteres
#✓Se comprobará que la letra este dentro del rango de letras usadas, sabiendo que las letras usadas son:
#T, R, W, A, G, M, Y, F, P, D, X, B, N, J, Z, S, Q, V, H, L, C, K, E.
#✓Se  comprobará que  la  letra  corresponde  al  número  del  DNI.
#Sabiendo  que  la letra se obtiene:calculando el resto de la división del número del DNI por 23.
#A cada  resultado  le  corresponde  una  letra:
#0=T;  1=R;  2=W;  3=A;  4=G;  5=M;  6=Y; 7=F;  8=P;  9=D;  10=X;  11=B;  12=N;  13=J;  14=Z;  15=S;
#16=Q;  17=V;  18=H;  19=L; 20=C; 21=K; 22=E.
#El  director  del  proyecto  nos  indica  que  el  programa
#tiene  que  resolverse  usando  el paradigma de la programación modular y nos sugiere utilizar tres funciones:
#una para comprobar  la  cantidad  de  caracteres,  otra  para  comprobar  si  la  letra  esta  dentro  del rango y
#la ultima para comprobar si la letra se corresponde al número del DNI.La validación será progresiva,
#de lo mas sencillo a lo mas complicado.
#En el momento en que falle una validación se avisara al usuario que el número introducido es incorrecto
#
#
#Se pide el DNI y con 'replace' se eliminan los espacios blancos, y con 'upper' nos convertimos los caracteres en mayusculas
#Se crea la variable global 'entrada' que se usa en las funciones sin modificarla
entradaUsuario = input("Su DNI, por favor: ")
entrada = entradaUsuario.replace(" ", "").upper()


def longitud():
    """
    Funcion para comprobar la longitud de la cadena introducida por el usuario
    'numCaracteres' es la cantidad de caracteres del DNI introducido
    Si son 9 caracteres la funcion termina y si no, sale del programa.
    """
    numCaracteres = len(entrada)
    if numCaracteres != 9:
        print(f"El numero introducido no es valido. Ha introducido {numCaracteres} caracteres y se necesitan 9.")
        exit()
    else:
        return()


def alfabeto():
    """
    Funcion para comprobar si la letra del DNI es valida.
    'letraEntrada1' es el ultimo caracter de la cadena introducida
    'testigo' es una variable para contar las veces que la letra de entrada no coincide con los elementos de la tupla
    Creamos una tupla con las letras permitidas.
    Si la letra del DNI coincide con algun elemento de la tupla la funcion termina
    Si la letra no coincide con al menos un elemento de la tupla, se sale del programa con mensaje de letra no valida
    """
    letrasValidas1 = ('T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E')
    letraEntrada1 = entrada[-1]
    testigo = 0
    for i in letrasValidas1:
        if letraEntrada1 == i:
            return()
        else:
            testigo += 1
    if testigo > 0:
        print(f"La letra \'{entrada[-1]}\' no es valida.")
        exit()


def coincidencia():
    """
    Funcion para comprobar si la letra del DNI corresponde al numero introducido
    'numDNI' es la parte numerica del DNI
    'letraEntrada2' es la letra del DNI
    'restoDiv' es el resto de la division del numero del DNI por 23
    Se crea un tupla, aprovechando que el indice de cada elemento puede servir como el numero correspondiente para esta letra.
    Se compara la letra del DNI con el elemento de la tupla con indice el resto de la division de
    la parte numerica del DNI por 23. Si coinciden, la funcion termina y si no
    coinciden, se sale del programa con el mensaje de combinacion no valida.
    """
    numDNI = int(entrada[0:8])
    letraEntrada2 = entrada[8]
    restoDiv = numDNI % 23
    letrasValidas2 = ('T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E')
    if letrasValidas2[restoDiv] != letraEntrada2:
        print(f"La combinacion de caracteres \'{entrada}\' no es valida.")
        exit()
    else:
        return()


#Se ejecutan las funciones. Cada funcion sale del programa si no se cumplen sus condiciones.
longitud()
alfabeto()
coincidencia()
print(f"El DNI \'{entrada}\' introducido es valido.")