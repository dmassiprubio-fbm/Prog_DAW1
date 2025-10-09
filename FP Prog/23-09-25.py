'--------------------------------------------------------------------------------------------'

num1 = int(input('introduce un numero '))
num2 = int(input('introduce otro numero '))

if num1 > num2:
    print(f"el mayor es {num1}")
    res = num1 - num2
    print(f'la diferencia es {res}')
elif num2 > num1:
    print(f"el mayor es {num2}")
    res = num2 - num1
    print(res)

'--------------------------------------------------------------------------------------------'

not1 = float(input("introduce la primera nota: "))
not2 = float(input("introduce la segunda nota: "))
not3 = float(input("introduce la tercera nota: "))

suma = not1 + not2 + not3
med = suma / 3
med_exacta = suma // 3
redondeo = round(med,2)
print(f"la media del alumno es {redondeo}")

if med >= 9:
    print(f"El alumno ha aprovado con matricula de honor con un {med_exacta}")
elif med >= 5:
    print(f"El alumno esta aprovado con un {med_exacta}")
elif med < 5:
    print(f"El alumno esta suspendido con un {med_exacta}")
    res = 5 - redondeo
    print(f"Le faltan {res} puntos para aprovar")

'--------------------------------------------------------------------------------------------'

num = int(input("introduce un num "))

resto = num % 2 
if resto == 0:
    print(f" {num} es par")
else:
    print(f" {num} es impar")

resto2 = num % 5
if resto2 == 0:
    print(f" {num} es multiplo de 5")
else:
    print(f" {num} no es multiplo de 5")

'--------------------------------------------------------------------------------------------'
## EJERCICIOS CLASSROOM ###
'--------------------------------------------------------------------------------------------'

altura = float(input('introduce en cm la altura del triangulo  '))
base = float(input('introduce en cm la medida de la base del triangulo  '))

area = (base * altura) / 2
areaR = round(area,2)
print(f'el area del triangulo es de {areaR} cm²')

'--------------------------------------------------------------------------------------------'

temperatura = float(input("introduce la temperatura en grados centigrados: "))

faren = temperatura * (9/5) + 32
print(f"la temperatura en fahrenheit da {faren} Fº")

'--------------------------------------------------------------------------------------------'

num = int(input("introduce un num "))

resto = num % 2 
if resto == 0:
    print(f" {num} es par")
else:
    print(f" {num} es impar")

'--------------------------------------------------------------------------------------------'

num1 = int(input('introduce un numero '))
num2 = int(input('introduce otro numero '))

if num1 > num2:
    print(f"el mayor es {num1}")
elif num2 > num1:
    print(f"el mayor es {num2}")