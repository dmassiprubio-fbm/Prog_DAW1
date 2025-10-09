from abc import ABC, abstractmethod
import csv
import os

class Game():
    def __init__(self, name:str, time:int, price:int, age:int, genre:str, status:str):
        self.name = name
        self.time = time
        self.price = price
        self.age = age
        self.genre = genre
        self.status = status

class saveInterface(ABC):
    @abstractmethod
    def __init__(self, ruta:str):
        self.ruta = ruta
        
    @abstractmethod
    def safe(self, games:list[Game]):
        pass

    @abstractmethod
    def load(self):
        pass

class CSVSave(saveInterface):
    def __init__(self, ruta):
        super().__init__(ruta)

    def safe(self, games:list[Game]):
        HEADER = ['name', 'time', 'price', 'age', 'genre', 'status']
        with open(self.ruta, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=HEADER)
            writer.writeheader()
            for game in games:
                writer.writerow(game.__dict__)

    def load(self):
        if os.path.exists(self.ruta):
            with open(self.ruta, 'r') as file:
                return list(csv.DictReader(file))
        return []

class Coleccion:
    def __init__(self, memory_method:saveInterface):
        self.games = []
        self.memory = memory_method

    def load_games(self):
        self.games = []
        for g in self.memory.load():
            self.games.append(Game(**g))

    def save_games(self, game:Game):
        self.games.append(game)
        self.memory.safe(self.games)

    def sesrch_game(self, game:Game):
        for game in self.games:
            if game.name == game.name:
                return game
        return None
   
    def update_game(self, udate_game:Game):
        for game in self.games:
            if game.name == game.name:
                 game.time = udate_game.time
                 game.price = udate_game.price
                 game.age = udate_game.age
                 game.genre = udate_game.genre
                 game.status = udate_game.status




def main():
    FILE_NAME = 'Coleccio_jocs.csv'
    HEADER = ['name', 'time', 'price', 'age', 'genre', 'status']
    my_csv = CSVSave(FILE_NAME)
    coleccion = Coleccion(my_csv)
    coleccion.load_games()

    while True:
        print('1 afegeix joc', sep="")  
        print('2 elimina joc', sep= "")  
        print('3 consulta joc', sep="") 
        print('4 actualitzar joc')
        print('5 consulta temps de un joc') 
        print('6 consulta preu de un joc') 
        print("7 conultar l'edat minima del joc")
        print("8 consultr el genere d'un joc") 
        print('9 consulta estat del joc')
        print('10 eliminar la coleccio i sortir', sep="") 

        option = input('Selecciona una opció: ')

        if option == '1':
            name = str(input('introdueix el nom del joc '))
            time = int(input('introdueix el temps de duracio del joc(en hores domes amb numeros, sense comes ni punts) '))
            price = int(input('introdueix el preu del joc '))
            age = int(input('introdueix la edat minima recomenada per jugar al joc '))
            genre = str(input('introdueix el genere del joc '))
            status = str(input('introdueix com dus el joc (pasat o no pasat)'))
            game = Game(name, time, price, age, genre, status)
            coleccion.save_games(game)

        elif option == '2':
                selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))
                with open(FILE_NAME, "r", newline="") as csv_file:
                    reader = list(csv.DictReader(csv_file))
                    reader.pop(selected)
                with open('Coleccio_jocs.csv', mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=HEADER)
                    writer.writeheader()
                    writer.writerows(reader)
        
        elif option == '3':
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

        elif option == '4':
            selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))
            name = str(input('introdueix el nom del joc '))
            time = int(input('introdueix el temps de duracio del joc '))
            price = int(input('introdueix el preu del joc '))
            age = int(input('introdueix la edat minima recomenada per jugar al joc '))
            genre = str(input('introdueix el genere del joc '))
            status = str(input('introdueix com dus el joc (pasat o no pasat)'))
            game = Game(name, time, price, age, genre, status)
            coleccion.update_game(game)

        elif option == '5':
            selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))
            with open(FILE_NAME, "r", newline="") as csv_file:
                reader = list(csv.DictReader(csv_file))
                seleccion = reader[selected]
                print(f"temps: {seleccion[HEADER[1]]}")

        elif option == '6':
            selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))
            with open(FILE_NAME, "r", newline="") as csv_file:
                reader = list(csv.DictReader(csv_file))
                seleccion = reader[selected]
                print(f"preu: {seleccion[HEADER[2]]}")

        elif option == '7':
            selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))
            with open(FILE_NAME, "r", newline="") as csv_file:
                reader = list(csv.DictReader(csv_file))
                seleccion = reader[selected]
                print(f"edat: {seleccion[HEADER[3]]}")
            
        elif option == '8':
            selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))
            with open(FILE_NAME, "r", newline="") as csv_file:
                reader = list(csv.DictReader(csv_file))
                seleccion = reader[selected]
                print(f"genere: {seleccion[HEADER[4]]}")

        elif option == '9':
            selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))
            with open(FILE_NAME, "r", newline="") as csv_file:
                reader = list(csv.DictReader(csv_file))
                seleccion = reader[selected]
                print(f"estat: {seleccion[HEADER[5]]}")
        
        elif option == '10':
            os.remove(FILE_NAME)
            break

main()