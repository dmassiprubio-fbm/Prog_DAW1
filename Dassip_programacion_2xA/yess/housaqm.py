# Houssam #

import json 
import os
from colorama import Fore, init
from abc import ABC, abstractmethod
init()

class Book:
    def __init__(self, title:str, author:str, desc:str, price:float, stock:int):
        self.title = title
        self.author = author
        self.desc = desc
        self.price = price
        self.stock = stock

class SaveInterface(ABC):
    @abstractmethod
    def __init__(self, ruta:str):
        self.ruta = ruta
        
    @abstractmethod
    def safe(self, books:list[Book]):
        pass

    @abstractmethod
    def load(self):
        pass

class JSONSave(SaveInterface):
    def __init__(self, ruta):
        super().__init__(ruta)

    def safe(self, books:list[Book]):
        with open(self.ruta, 'w') as file:
            json.dump(books, file, indent=4)

    def load(self):
        if os.path.exists(self.ruta):
            with open(self.ruta, 'r') as file:
                return json.load(file)
        return {}


class Book:
    def __init__(self, title:str, author:str, desc:str, price:float, stock:int):
        self.title = title
        self.author = author
        self.desc = desc
        self.price = price
        self.stock = stock

class Library:
    def __init__(self, memory_methon:SaveInterface):
        self.books = []
        self.memory = memory_methon

    def load_books(self):
        self.books = []
        for b in self.memory.load().values():
            self.books.append(Book(**b))

    def save_book(self, book:Book):
        self.books.append(book)
        my_dictionari = {}
        element = 1
        for b in self.books:
            my_dictionari[element] = b.__dict__
            element +=1
        self.memory.safe(my_dictionari)

    def search_info(self, title:str):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def update_info(self, update_book:Book):
        for book in self.books:
            if book.title == update_book.title:
                book.author = update_book.author
                book.price = update_book.price
                book.desc = update_book.desc
                book.stock = update_book.stock





def main():
    ruta_doc = "Llibreria.json"
    library = Library(JSONSave(ruta_doc))
    library.load_books()  # Cargar la biblioteca al inicio

    while True:
        print(Fore.LIGHTWHITE_EX + "1. Afegir llibre")
        print("2. Consultar la informacio del llibre")
        print("3. Actualizar llibre")
        print("4. Consultar tots el llibres")
        print("5. Borrar llibre")
        print("6. sortir" + Fore.RESET)

        option = input("Selecciona una opció: ")

        if option == "1":
            title = input("Introdueix el títol del llibre: ")
            author = input("Introdueix el autor llibre: ")
            description = input("Introdueix la descripció del llibre: ")
            price = float(input("Introdueix el preu del llibre: "))
            stock = int(input("Introdueix el stock del llibre: "))
            book = Book(title, author, description, price, stock)
            library.save_book(book)

            print(Fore.GREEN + "Llibre afegit amb èxit!" + Fore.RESET)

        elif option == "2":
            title = input("Introdueix el títol del llibre per consultar la informacio: ")
            book = library.search_info(title) 
            if book is not None:
                print(Fore.CYAN + f"Autor: {book.author}" + Fore.RESET)
                print(Fore.CYAN + f"Descripció: {book.description}" + Fore.RESET)
                print(Fore.CYAN + f"Preu: {book.preu}" + Fore.RESET)
                print(Fore.CYAN + f"Stock: {book.stock}" + Fore.RESET)
            else:
                print(Fore.RED + "El llibre no existeix." + Fore.RESET)

        elif option == "3":
            title = input("Introdueix el títol del llibre que vols actualitzar: ")
            if title in library:
                author = input("Introdueix el nou autor del llibre: ")
                description = input("Introdueix la nova descripció del llibre: ")
                price = float(input("Introdueix el nou preu del llibre: "))
                stock = int(input("Introdueix el nou stock del llibre: "))
                book = Book(title, author, description, price, stock)
                library.save_book(book)

                print(Fore.GREEN + "Llibre actualitzat amb èxit!" + Fore.RESET)
            else:
                print(Fore.RED + "El llibre no existeix." + Fore.RESET)

            
        elif option == "4":
            if library:
                print(Fore.LIGHTYELLOW_EX + "Llibres disponibles:")
                for book in library.books:
                    print(Fore.LIGHTGREEN_EX + f"Títol: {book.title}\nAutor: {book.author}" + Fore.RESET)
            else:
                print(Fore.RED + "No hi ha llibres disponibles." + Fore.RESET)

        elif option == "5":
            title = input("Introdueix el títol del llibre que vols esborrar: ")
            if title in library:
                del library[title]
                library.save_book(library)
                print(Fore.GREEN + "Llibre esborrat amb èxit!" + Fore.RESET)
            else:
                print(Fore.RED + "El llibre no existeix." + Fore.RESET)

        elif option == "6":
            print("Programa Tancat")
            break

        else:
            print(Fore.RED + "Opció no vàlida. Si us plau, selecciona una opció del menú." + Fore.RESET)

main()