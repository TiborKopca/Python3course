print('EN:Type numbers, separated by point.')
# print('ES:Escriba unos numeros, separado con punto.')
number = float(input())
print(f'EN:Those numbers : {number} is of type {type(number)}')
# print(f'ES:Esos numeros : {number} son de tipo {type(number)}')
print()
print('EN:Now type numbers separated by comma.')
# print('ES:Ahora escriba unos numeros separado con coma.')
number2 = input()
print(f'EN:The number2 you typed is {number2} and of type {type(number2)}.')
# print(f'ES:Los numeros2 usted escribo son {number2} y de tipo {type(number2)}.')
print('EN:Now we replace the "," with "."')
# print('ES:Ahora reemplazamos "," con "."')
number2 = number2.replace(',' , '.')
print(f'EN:The number2 : {number2} is changed by replace() method to use point instead comma.')
# print(f'ES:El numero2 : {number2} se cambia con metoda replace() para utilizar un punto en caso de coma.')