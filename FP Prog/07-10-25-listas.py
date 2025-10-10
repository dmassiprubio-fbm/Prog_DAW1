import numpy as np

# ###1###
# lista = []
# word = ()
# while word != (""):
#     word = input('introduce un palabra: ')
#     lista.append(word)   
#del lista[-1]
# print(f"Las palabras que has escrito son {lista}")

# ###2###

# lista = []
# num = ()
# while num != ("Salir"):
#     num = input('introduce un numero:("Salir" para tarminar) ')    
#     lista.append(num)
#del lista[-1]
# print(f"los numeros que has introducuido son {lista}")

# ###3###

# lista = []
# nota = (0)
# while nota in np.arange (0,11,0.1):
#     nota = float(input('introduce una nota: (se redondeara a 1 decimal) '))
#     notaR = round(nota, 1)
#     lista.append(notaR)
# del lista[-1]
# print(f'las notas que has sintroducido son {lista}')

# ###4###

# lista = []
# num = int(input('introduce un numero: '))
# lista.append(num)
# num2 = int(input(f'introduce un numero mayor que {num}: '))
# while num >= num2:
#     num2 = int(input(f'introduce un numero mayor que {num}, el anterior no lo era: '))

# lista.append(num2)

# print(f'Los numero son {lista[0]} y {lista[1]}')

###5###

# lista = []
# num = int(input('introduce un numero: '))
# lista.append(num)
# num = int(input(f'introduce un numero mayor que {lista[-1]}: '))

# while num > lista[-1]:
#     lista.append(num)
#     num = int(input(f'introduce un numero mayor que {lista[-1]}: '))
    

# print("Los numero introduciods son: ", ", ".join(str(i)for i in lista))

# ###6###

# lista = []
# num = int(input("introduce un numero: "))
# num2 = int(input("introduce un numero: "))
# num3 = (num)
# lista.append(num)
# lista.append(num2)

# while num3 in range(num, num2 + 1):
#     num3 = int(input(f"introduce un numero entre {num} y {num2}: "))
#     lista.append(num3)

# print("Los numero introduciods son: ", ", ".join(str(i)for i in lista))

# ###7###

# lista = []
# num = int(input('Introduce un numero limite:' ))
# contador = (0)

# while contador < num:
#     num2 = int(input("introdcue un numero para sumar: "))
#     lista.append(num2)
#     contador = contador + num2

# print(f"Has llegado a {num} introduciendo estos numero: ", ", ".join(str(i)for i in lista))

# ###8###

# lista = []
# num = int(input("Introduce un numero limite: "))
# contador = (0)

# while contador != num:
#     num2 = int(input("introdcue un numero: "))
#     contador = num2 + contador
#     if contador <= num:
#         lista.append(num2)
#     elif contador > num:
#         print('sobrepasas el limite')
#         contador = contador - num2

# print(f"Has llegado a {num} introduciendo estos numero: ", ", ".join(str(i)for i in lista))

###9###

