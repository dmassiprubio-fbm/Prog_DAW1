import csv
import os
from colorama import Fore,init


init()

print(Fore.BLUE,'BENVINGUT A LA TEVA COLECCIO DE VIDEOJOCS 🎮👾🕹️')
print(Fore.WHITE + 'Selecciona una opcio del 1 al 13: ')

FILE_NAME = 'Coleccio_jocs.csv'


HEADER = ['nom', 'temps', 'preu', 'edat', 'genere', 'estat']
if not os.path.isfile('Coleccio_jocs.csv'):
    with open('Coleccio_jocs.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER)
        writer.writeheader()

while True:
    print(Fore.GREEN,'1 afegeix joc', sep="")  
    print(Fore.RED,'2 elimina joc', sep= "")  
    print(Fore.WHITE,'3 consulta joc', sep="") 
    print('4 actualitzar joc')
    print('5 consulta temps de un joc') 
    print('6 consulta preu de un joc') 
    print("7 conultar l'edat minima del joc")
    print("8 consultr el genere d'un joc") 
    print('9 consulta estat del joc')
    print(Fore.YELLOW,'10 eliminar la coleccio i sortir', sep="")  
    print(Fore.GREEN,'11 sortir sense eliminar', sep="")  
    print("el nom i el genere s'escriu domes en lletres i el tems,preu i edat s'escriu domes un nombre sense res més")
    print('no es pot fer res sense afegir el primer joc')
    option = input(Fore.WHITE,)

    def var():
        name = str(input('introdueix el nom del joc '))
        time = int(input('introdueix el temps de duracio del joc '))
        price = int(input('introdueix el preu del joc '))
        age = int(input('introdueix la edat minima recomenada per jugar al joc '))
        genre = str(input('introdueix el genere del joc '))
        estat = str(input('introdueix com dus el joc (pasat o no pasat)'))
        datos = {'nom':name,
                'temps': time,
                'preu': price,
                'edat': age,
                'genere': genre,
                'estat' : estat}
        return datos
    def one():
        with open ('Coleccio_jocs.csv','a', encoding='utf-8') as colecction_the_games:
            Colecction_games = csv.DictWriter(colecction_the_games, fieldnames=HEADER)
            Colecction_games.writerow(var())

    def three():
        selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))
        with open(FILE_NAME, "r", newline="") as csv_file:
            reader = list(csv.DictReader(csv_file))
            seleccion = reader[selected]
            print(f"nom: {seleccion[HEADER[0]]}")
            print(f"temps: {seleccion[HEADER[1]]}")
            print(f"preu: {seleccion[HEADER[2]]}")
            print(f"edat: {seleccion[HEADER[3]]}")
            print(f"genere: {seleccion[HEADER[4]]}")
            print(f"estat: {seleccion[HEADER[5]]}")
          
    def five():
        selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))
        with open(FILE_NAME, "r", newline="") as csv_file:
            reader = list(csv.DictReader(csv_file))
            seleccion = reader[selected]
            print(f"temps: {seleccion[HEADER[1]]}")
    def six():
        selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))
        with open(FILE_NAME, "r", newline="") as csv_file:
            reader = list(csv.DictReader(csv_file))
            seleccion = reader[selected]
            print(f"preu: {seleccion[HEADER[2]]}")
    def seven():
        selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))
        with open(FILE_NAME, "r", newline="") as csv_file:
            reader = list(csv.DictReader(csv_file))
            seleccion = reader[selected]
            print(f"edat: {seleccion[HEADER[3]]}")
    def eigth():
        selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))
        with open(FILE_NAME, "r", newline="") as csv_file:
            reader = list(csv.DictReader(csv_file))
            seleccion = reader[selected]
            print(f"genere: {seleccion[HEADER[4]]}")  
    def four():
        selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))
        with open(FILE_NAME, "r", newline="") as csv_file:
            reader = list(csv.DictReader(csv_file))
            seleccion = reader[selected]
            new_game = {}
            print(f"nom actual: {seleccion[HEADER[0]]}")
            new_game[HEADER[0]] = input("introdueix l'actulitzacio: ")
            print(f"temps actual: {seleccion[HEADER[1]]}")
            new_game[HEADER[1]] = input("introdueix l'actulitzacio: ")
            print(f"preu actual: {seleccion[HEADER[2]]}")
            new_game[HEADER[2]] = input("introdueix l'actulitzacio: ")
            print(f"edat actual: {seleccion[HEADER[3]]}")
            new_game[HEADER[3]] = input("introdueix l'actulitzacio: ")
            print(f"genere actual: {seleccion[HEADER[4]]}") 
            new_game[HEADER[4]] = input("introdueix l'actulitzacio: ")
            print(f"estat actual: {seleccion[HEADER[5]]}") 
            new_game[HEADER[5]] = input("introdueix l'actulitzacio: ")  
            reader[selected] = new_game
            with open('Coleccio_jocs.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=HEADER)
                writer.writeheader()
                writer.writerows(reader)
            
    def two():
        selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))
        with open(FILE_NAME, "r", newline="") as csv_file:
            reader = list(csv.DictReader(csv_file))
            reader.pop(selected)
            with open('Coleccio_jocs.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=HEADER)
                writer.writeheader()
                writer.writerows(reader)
    def nine():
        selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))
        with open(FILE_NAME, "r", newline="") as csv_file:
            reader = list(csv.DictReader(csv_file))
            seleccion = reader[selected]
            print(f"estat: {seleccion[HEADER[5]]}")            
    if option == '1':
        one()
    elif option == '2':
        two()
    elif option == '3':
        three()
    elif option == '4':
        four()
    elif option == '5':
        five()
    elif option == '6':
        six()
    elif option == '7':
        seven()
    elif option == '8':
        eigth()
    elif option == '9':
        nine()
    elif option == '10':
        print(Fore.LIGHTRED_EX,'ELIMINANT ☠️☠️º')
        print(Fore.LIGHTBLUE_EX,'Sortinit de la coleccio, GRACIES !!!')
        os.remove('Coleccio_jocs.csv')
        break
    elif option == '11':
        print(Fore.LIGHTBLUE_EX,'Sortinit de la coleccio, GRACIES !!! 😎😎')
        break



       
    
