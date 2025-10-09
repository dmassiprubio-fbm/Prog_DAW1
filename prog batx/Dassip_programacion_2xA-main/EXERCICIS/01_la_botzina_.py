'''
Escriu un programa que mostri per consola els nombres de l’1 al 100 (ambdós inclosos
i amb un bot de línia entre cada nombre), substituint els nombres per “FIZZ” o “BUZZ”
segons les següents regles:
- Múltiples de 3 per la paraula “FIZZ”.
- Múltiples de 5 per la paraula “BUZZ”.
- Múltiples de 3 i de 5 per la paraula “FIZZ BUZZ”.

Entrada i sortida:
Aquest programa no tendrà cap entrada. El programa mostrarà directament els
nombres d’1 a 100 seguint les instruccions de l’enunciat.
'''



p3 = 'FIZZ'
p5 = 'BUZZ'
contador = 0

for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
             print(p3,p5)
        elif num % 3 == 0:
            print(p3)
        elif num % 5 == 0:
            print(p5)
        else:
             contador = contador + 1
             print(num)


