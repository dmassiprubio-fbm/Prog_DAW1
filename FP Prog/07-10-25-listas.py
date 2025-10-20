import numpy as np
import random

###1###
lista = []
word = ()
while word != (""):
    word = input('introduce un palabra: ')
    lista.append(word)   
del lista[-1]
print(f"Las palabras que has escrito son {lista}")

###2###

lista = []
num = ()
while num != ("Salir"):
    num = input('introduce un numero:("Salir" para tarminar) ')    
    lista.append(num)
del lista[-1]
print(f"los numeros que has introducuido son {lista}")

###3###

lista = []
nota = (0)
while nota in np.arange (0,11,0.1):
    nota = float(input('introduce una nota: (se redondeara a 1 decimal) '))
    notaR = round(nota, 1)
    lista.append(notaR)
del lista[-1]
print(f'las notas que has sintroducido son {lista}')

###4###

lista = []
num = int(input('introduce un numero: '))
lista.append(num)
num2 = int(input(f'introduce un numero mayor que {num}: '))
while num >= num2:
    num2 = int(input(f'introduce un numero mayor que {num}, el anterior no lo era: '))

lista.append(num2)

print(f'Los numero son {lista[0]} y {lista[1]}')

###5###

lista = []
num = int(input('introduce un numero: '))
lista.append(num)
num = int(input(f'introduce un numero mayor que {lista[-1]}: '))

while num > lista[-1]:
    lista.append(num)
    num = int(input(f'introduce un numero mayor que {lista[-1]}: '))
    

print("Los numero introduciods son: ", ", ".join(str(i)for i in lista))

###6###

lista = []
num = int(input("introduce un numero: "))
num2 = int(input("introduce un numero: "))
num3 = (num)
lista.append(num)
lista.append(num2)

while num3 in range(num, num2 + 1):
    num3 = int(input(f"introduce un numero entre {num} y {num2}: "))
    lista.append(num3)

print("Los numero introduciods son: ", ", ".join(str(i)for i in lista))

###7###

lista = []
num = int(input('Introduce un numero limite:' ))
contador = (0)

while contador < num:
    num2 = int(input("introdcue un numero para sumar: "))
    lista.append(num2)
    contador = contador + num2

print(f"Has llegado a {num} introduciendo estos numero: ", ", ".join(str(i)for i in lista))

###8###

lista = []
num = int(input("Introduce un numero limite: "))
contador = (0)

while contador != num:
    num2 = int(input("introdcue un numero: "))
    contador = num2 + contador
    if contador <= num:
        lista.append(num2)
    elif contador > num:
        print('sobrepasas el limite')
        contador = contador - num2

print(f"Has llegado a {num} introduciendo estos numero: ", ", ".join(str(i)for i in lista))

###9###

lista = []
lista2 = []
nombre = input('introduce un nombre: ')
nombre = nombre.lower()

while nombre != "s":
    tel = input('introduce un numero telefonico: ')
    cant = len(tel)
    if cant == 9:
        lista2 = [nombre, tel]
        lista.append(lista2)
    else:
        print('numero de telefono incorrecto, vuelve a intentarlo')
    nombre = input('introduce un nombre: ')
    nombre = nombre.lower()

for contaactos in lista:
    print('..................................')
    print(f'Nombre-{contaactos[0]} : Numero-{contaactos[1]}')


###10###

lista = []
lista2 = []
nombre = input('introduce el nombre del alumno: ' )

while nombre != "":
    lista2.append(nombre)
    nota = (0)
    while nota in np.arange (0,11,0.1):
        nota = round(float(input('introduce una nota(se redondeara a 1 decimal)')))
        lista2.append(nota)
    lista.append(lista2)
    nombre = input('introduce el nombre del alumno: ' )

for notas in lista:
     print('..................................')
     print(f'Nombre: {notas[0]}')
     notas.remove(notas[0])
     print(f"Las notas de este alumno son: ", ", ".join(str(i)for i in notas))

###11###

valor_min = int(input(' introduce el valor min: '))
valor_max = int(input(' introduce el valor max: '))
num = random.randint(valor_min, valor_max + 1)
contador = 0
numero = 0

while numero != num:
    numero = int(input(f'introduce un numero del {valor_min} al {valor_max}: '))
    if numero == num:
            print(f"l'has endivinat, era el numero {num}")
    elif numero < num:
            print(f"el numero per endivinar es mes gran que {numero}")
            contador+=1
    elif numero > num:
            print(f" el numero per endivinar es mes petit que {numero}")
            contador+=1
print(f'ya has utilitzat els {contador} intents, per endivinar {num}')

###12###

valor_max = int(input('introduce un avlor maximo: '))
valor_min = int(input('introduce un valor min: '))

print(f'piensa en un numero entre el {valor_min} y {valor_max}')

resultado = 0
print('para jugar con la maquina recuerda: 1 para decire que es menor, 2 para decirle que es mayor, 3 para decirle que es correcto')

while resultado != 3:
    numero = random.randint(valor_min, valor_max )
    print (numero)
    resultado = int(input('es correcto? '))
    if resultado == 3:
        print('Igual, gracias por jugar')
    elif resultado == 2:
          valor_min = numero +1 
    elif resultado == 1:
          valor_max = numero -1

###13###

lista = []
verdadero = True

while verdadero == True:
    numero = int(input('introduce un numero primo(parara cuando introduzcas una no primo): '))
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            verdadero = False
            break
    if es_primo:
        lista.append(numero)
    else:
        verdadero = False    

del lista[-1]
print(lista)   