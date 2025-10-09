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

lista = []
num = int(input('introduce un numero: '))
lista.append(num)


while num >= lista[-1]:

    num = int(input(f'introduce un numero mayor que {lista[-1]}: '))
    lista.append(num)



print(lista)