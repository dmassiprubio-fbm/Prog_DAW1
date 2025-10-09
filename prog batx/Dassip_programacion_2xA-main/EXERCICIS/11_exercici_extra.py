'''
DIFICULTAT EXTRA (Puntua si el resols totsol):

5️⃣ Desenvolupa un programa de gestió de vendes que emmagatzema les seves dades en un arxiu .txt.
6️⃣ Cada producte es guarda en una línia de l'arxiu de la manera següent:

    [nom_producte], [quantitat_venuda], [preu].
    Seguint aquest format, i mitjançant terminal, ha de permetre afegir, consultar, actualitzar, eliminar productes i sortir.
    També ha d'haver-hi opcions per a calcular la venda total i per producte.
    L'opció sortir esborra el .txt.
'''
   
import os

file_name = 'el_moro.txt'
open(file_name, 'a')
while True:
    print('1 Afegir producte')
    print('2 Consultar producte')
    print('3 Actualitzar producte')
    print('4 Borrar producte')
    print('5 Mostrar producte')
    print('6 Calcular venta total')
    print('7 Calcular venta per producte')
    print('8 Sortir')

    opcion = input('Seleciona unaopcio entre el 1 i el 8: ')
    


    if opcion == '1':
            text = input('afeiegix el nom del producte: ')
            text2 = input('afeiegix la cantidat del producte: ')
            text3 = input('afeiegix el preu del producte: ')
            with open('el_moro.txt','a') as file:
                file.write(f'{text}, {text2}, {text3}\n')
    elif opcion == '2':
        name = input('nom: ')
        with open(file_name, 'r') as file:
            for line in file.readlines():
                if name == line.split(', ')[0]:
                    print(line)
                    break        
    elif opcion == '3':
        text = input('afeiegix el nom del producte: ')
        text2 = input('afeiegix la cantidat del producte: ')
        text3 = input('afeiegix el preu del producte: ')
        products = []
        with open(file_name, 'r') as file:
            products = file.readlines()
        with open(file_name, 'w') as file:
            for product in products:
                if product.split(', ')[0] == name:
                    file.write(f'{text}, {text2}, {text3}\n')
    elif opcion == '4':
        name = input('nom: ')
        products = []
        with open(file_name, 'r') as file:
            products = file.readlines()
        with open(file_name, 'w') as file:
            for product in products:
                if product.split(', ')[0] != name:
                    file.write(product)
    elif opcion == '5':
        with open(file_name, 'r') as file:
            print(file.read())
    elif opcion == '6':
        total = 0
        with open(file_name, 'r') as file:
            for product in file.readlines():
                components = line.split(', ')
                quantity = int(components[1])
                price = float(components[2])
                total += quantity * price
            print(total)
    elif opcion == '7':
        name = input('nom: ')
        with open(file_name, 'r') as file:
            for line in file.readlines():
                if name == line.split(', ')[0]:
                    print(int(line.split(', ')[1])*float(line.split(', ')[2]))
                    break 
    elif opcion == '8':
        print('sortint del arxiu, graies per utilitzar aquets programa')
        os.remove('el_moro.txt')    