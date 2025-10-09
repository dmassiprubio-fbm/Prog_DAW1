import random

num = random.randint(1,100)
contador = 0
intentos = 3

while contador < 3:
    numero = int(input(f'introduce un numero del 1 al 99 (tens {intentos} intents): '))
    if numero == num:
            print(f"l'has endivinat, era el numero {num}")
            contador = 3
    elif numero < num:
            print(f"el numero per endivinar es mes gran que {numero}")
            contador+=1
            intentos-=1
    elif numero > num:
            print(f" el numero per endivinar es mes petit que {numero}")
            contador+=1
            intentos-=1
    if intentos == 0 :
        print(f'ya has utilitzat els 3 intents, el numero era {num}')