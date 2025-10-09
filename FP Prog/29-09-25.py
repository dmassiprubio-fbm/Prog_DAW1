num = int(input('Introduce un numero: '))
if num == 0:
    print('el numero es 0')
elif num > 0:
    print(f'{num} es positivo')
elif num < 0:
    print(f'{num} es negativo')

'---------------------------------------------------------'

num1 = int(input('introduce un numero: '))
num2 = int(input('introduce un numero: '))

if num1 < num2:
    print(f'{num2} es mas garnde que {num1}')
elif num1 > num2:
    print(f'{num1} es mas garnde que {num2}')

'---------------------------------------------------------'

edat = int(input('introduce tu edad: '))

if edat < 18:
    print('lo siento eres menor y no puedes votar')
elif 18 <= edat < 65:
    print(f'perfecto con {edat} años puedes votal')
elif edat >= 65:
    print(f'con {edat} puedes votar y estas jubilado')

'---------------------------------------------------------'

letra = input('introduce una letra: ')


if letra.isupper():
    letra2 = letra.lower()
    print(letra2)
elif letra.islower():
    letra2 = letra.upper()
    print(letra2)
elif not letra.isalpha():
    print('error esto no es una letra')

