'''Modulo que calcula la edad de la mascota y la presentación de la fecha'''
from datetime import datetime

def age(date):             #date is in format dd/mm/yyyy
    '''Calcula la edad de la mascota'''
    today = datetime.now()
    # print(today.year)
    # print(date)
    petsAge = today.year - date.year
    # print('the pet has: ',petsAge,'years.')
    return petsAge


#tests
mydate = '23/12/1999'
format = '%d/%m/%Y'
mydatetime = datetime.strptime(mydate, format)
print(age(mydatetime))



