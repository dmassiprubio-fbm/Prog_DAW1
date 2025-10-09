nom = input('introduce tu nombre: ')
print(f'el teu nom es {nom}')

'-------------------------------------------------------------------'

esp = int(input('introduce el recorrido del coche en km: '))
hora= int(input('introduce el tiempo que ha tardado en recorrer h: '))
if esp == 0: ###
    print('No es pot fer en 0 hores') ###
else: ###
    res = esp / hora
    redondeo = round(res, 2)
    print(f'la velocidad media es de {redondeo} km/h')

'-------------------------------------------------------------------'

num1 = 1
num2 = 3.5
word1 = 'hola'
word2 = True

print(type(num1))
print(type(num2))
print(type(word1))
print(type(word2))

'-------------------------------------------------------------------'

nota1 = int(input('intoduce una nota: '))
nota2 = int(input('intoduce una nota: '))
nota3 = int(input('intoduce una nota: '))

res = (nota1 + nota2 +nota3) / 3 ###
redondeo = round(res, 0) ###
print(f'la media es de {redondeo}') ###

'-------------------------------------------------------------------'

num = int(input('introduce un numero'))

if num <= 999:
    print('perfecte')
else:
    print(F'ERROR el numero {num} te mès de 3 ciferes')

'-------------------------------------------------------------------'

name_prodcut = input('introduce el nombre del producto: ')
price = int(input('introduce el precio del producto: '))
final_price = price + (price * 0.21)
print(f'el precio de {name_prodcut} con el 21% del IVA es de {final_price}€')

'-------------------------------------------------------------------'

day = int(input('introduce el numero del dia: '))
month = int(input('introduce el numero del mes: '))
year = input('introduce el nuero del año: ')



if month == 1 or month ==3 or month ==5 or month ==7 or month ==8 or month ==10 or month ==12:
    if day <= 31:
        print(f'{day}/{month}/{year} fecha correcta')
    else:
        print(f'{day}/{month}/{year} fecah incorrecta')
elif month == 4 or month ==6 or month ==9 or month ==11:
    if day <= 30:
        print(f'{day}/{month}/{year} fecha correcta')
    else:
        print(f'{day}/{month}/{year} fecah incorrecta')
elif month == 2:
    if day <= 28:
        print(f'{day}/{month}/{year} fecha correcta')
    else:
        print(f'{day}/{month}/{year} fecah incorrecta')
