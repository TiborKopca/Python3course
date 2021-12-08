def selectNumbers(stringOfNumbers):
    '''The function select first 8 characters from the string and change them to numbers'''
    try:
        numbers = int(stringOfNumbers[:8])     #we take out the numbers from the string
    except ValueError:
        print("Excepción ValueError")
        print("El DNI introducido ", stringOfNumbers, " no es un formato correcto.")
        numbers = -1                    #if there is error, return value that later the code will read as error
        return numbers
    else:
        return numbers