#!/usr/bin/env python
#Tema 13, ejercicio 13: El Ministerio del Interior desea realizar una actualización del programa para la validación del DNI español.
#Hay  que  rehacer  el  programa  del  ejercicio  12utilizando  el  paradigma  de  la  programación Modular.
#Cada una de las funciones ira dentro de un módulo.Se desarrollará una función nueva que tome el numero introducido
#por el usuario y lo devuelva en MAYÚSCULAS con los espacios en blanco, los puntos, los guiones y los guiones bajos
#que el usuario introduzca junto con el número del DNI ELIMINADOS.
#El programa principal importara los módulosy ejecutara las funciones.
#Primero se importan los modulos. El modulo 'depurar' crea la variable global 'entrada', la cual se usa en los demas modulos
#con 'depurar.entrada[]' se llama a la variable global creada en el moduo 'depurar'
import alfabeto
import coincidencia
import depurar
import longitud
def main():
    depurar.limpieza()
    longitud.recorte()
    alfabeto.alfabetizar()
    coincidencia.validacion()
    print(f"El DNI introducido \'{depurar.entrada}\' es valido.")
if __name__ == "__main__":
    main()
#Se usa una variable global 'entrada' cual es el numero de entrada pasado por los filtros de ' ., -_' en el modulo 'depurar'. 
#Este modulo se ejecuta primero y asi tenemos una variable global para usar entre todos los modulos
#Para conseguir esto, primero se tiene que crear una variable global 'entrada' en el dicho modulo ('depurar')
#Se importa el modulo 'depurar' en cada modulo en que se va a usar la variable 'entrada'
#import depurar
#La llamada a esta variable global en los demas modulos se hace de la manera: nombreDeModulo.nombreDeVariableGlobal
#ejemplos:
#En modulo alfabeto.py -> letraEntrada1 = depurar.entrada[-1]
#En modulo coincidencia.py -> letraEntrada2 = depurar.entrada[8] y numDNI = int(depurar.entrada[0:8])
#En modulo longitud.py -> numCaracteres = len(depurar.entrada)
#En general para usar una variable entre diferentes modulos primero se tiene que crear esta variable en el primer modulo
#que se ejecuta en el programa. Luego en cada modulo que utiliza esta variable global se tiene que importar el modulo donde
#se ha creado la variable global.
#Mas detallado en: https://instructobit.com/tutorial/108/How-to-share-global-variables-between-files-in-Python