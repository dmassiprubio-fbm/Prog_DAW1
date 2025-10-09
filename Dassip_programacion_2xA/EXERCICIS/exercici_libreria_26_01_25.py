import csv
import os

"""
Crear una aplicació bàsica per gestionar una biblioteca digital. La funcionalitat inclou:
1️⃣ Afegir llibres.
2️⃣ Llistar llibres disponibles.
3️⃣ Permetre la devolució o préstec d'un llibre.
4️⃣ Generar un informe senzill de l'estat de la biblioteca.
Aplicar cada principi per estructurar el codi de forma clara, escalable i fàcil de mantenir.

Passos de l'exercici:
1️⃣ Single Responsibility Principle (SRP)
Tasca: Crear una classe per representar un llibre (Book) i una altra per gestionar la biblioteca (Library).
Punt clau: Cada classe ha de tenir una única responsabilitat.
#La classe Book només s'encarrega de representar informació d'un llibre (títol, autor, estat).
La classe Library només gestiona lògica com afegir llibres, llistar-los, etc.
2️⃣ Open/Closed Principle (OCP)
Tasca: Permetre afegir funcionalitats (com nous tipus d'informes) sense modificar el codi existent.
Punt clau: Utilitzar una interfície per a la generació d'informes (ReportGenerator) i implementar-ne una versió bàsica que generi informes en format text. Es poden afegir altres tipus (PDF, JSON) en el futur.
3️⃣ Liskov Substitution Principle (LSP)
#Tasca: Crear subclasses de Book (per exemple, DigitalBook i PrintedBook) i assegurar que poden substituir la classe base sense alterar el comportament de l'aplicació.
Punt clau: Les subclasses han de ser completament compatibles amb la classe base.
4️⃣ Interface Segregation Principle (ISP)
Tasca: Definir interfícies específiques per rols diferents.
Exemple: Crear interfícies com Borrowable per gestionar llibres que es poden prestar, però no aplicar aquesta interfície a llibres digitals que no necessiten préstec físic.
5️⃣ Dependency Inversion Principle (DIP)
Tasca: Utilitzar la inversió de dependència per desacoblar classes concretes.
Exemple: La classe Library no ha de dependre d'una implementació concreta d'un generador d'informes, sinó d'una interfície abstracta (ReportGenerator).
"""

from abc import ABC, abstractmethod

FILE_NAME = "Informe_d'estat_de_la_biblioteca(Llibres_digitals).csv"
HEADER = ['titol', 'autor', 'valoracio'] #Num.rentat
if not os.path.isfile("Informe_d'estat_de_la_biblioteca(Llibres_digitals).csv"):
    with open("Informe_d'estat_de_la_biblioteca(Llibres_digitals).csv", mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER)
        writer.writeheader()

FILE_NAME2 = "Informe_d'estat_de_la_biblioteca(Llibres_fisics).csv"
HEADER2 = ['titol', 'autor', 'estat', 'fisic'] 
if not os.path.isfile("Informe_d'estat_de_la_biblioteca(Llibres_fisics).csv"):
    with open("Informe_d'estat_de_la_biblioteca(Llibres_fisics).csv", mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER2)
        writer.writeheader()

def varD():
    title = str(input('introdueix el titol del llibre '))
    autor = str(input("introdueix l'autor del llibre "))
    #rented = str(input('introdueix si el llibre esta llogat o no '))
    ratings = int(input('introdueix la valoracio del llibre '))
    datos = {'titol':title,
            'autor': autor,
            'valoracio' : ratings}  #'llogat': rented,
    return datos

def varP():
    title = str(input('introdueix el titol del llibre '))
    autor = str(input("introdueix l'autor del llibre "))
    state = str(input('introdueix si el llibre esta llogat o no '))
    phisical = str(input("introdueix l'estat fisic del llibre "))
    datos = {'titol':title,
            'autor': autor,
            'estat': state,
            'fisic': phisical}
    return datos


class BookInterface(ABC):
    @abstractmethod
    def infoB(self, title, autor):
        pass

#class RentedInterface(ABC):
    #@abstractmethod
    #def rent(self, rented):
        #pass

class RatingsInterface(ABC):
    @abstractmethod
    def rating(self, ratings):
        pass

class StateInterface(ABC):
    @abstractmethod
    def state(self, state):
        pass

class PhisicalInterface(ABC):
    @abstractmethod
    def phisic(self, physical):
        pass

class digitalbook(BookInterface, RatingsInterface): #RentedInterface
    def __init__(self, title, autor, ratings): #rented
        self.title = title
        self.autor = autor
        #self.rented = rented
        self.ratings = ratings
        
    def infoB(self, title, autor):
        self.title = title
        self.autor = autor
        print(f"{self.title} es el titol d'aquest llibre")
        print(f"en {self.autor} es el autor que va escriure aquest llibre")
       
    #def rent(self, rented,):
        #print(f"han rentat aquets llibre {self.rented} vegades")

    def rating(self, ratings):
        self.ratings = ratings
        print(f"s'ultima valòracio donada a aquest llibre es de {self.ratings} estrelles")
        
class phisicalbook(BookInterface, StateInterface):
    def __init__(self, title, autor, state, phisical):
        self.title = title
        self.autor = autor
        self.state = state #llogat o no
        self.phisical = phisical #estat fisic
        
    def infoB(self, title, autor):
        self.title = title
        self.autor = autor
        print(f"{self.title} es el titol d'aquest llibre")
        print(f"en {self.autor} es el autor que va escriure aquest llibre")
    
    def state(self, state,):
        self.state = state
        print(f"el llibre es troba {self.state}")
    
    def phisic(self, phisical):
        self.phisical = phisical
        print(f"el llibre es troba en estat {self.phisical}")
        


class logisitc_of_library(ABC):
    pass

class Add_Digital_BookInterface(logisitc_of_library):      
    def add_Dbook(self):
        title = input("Introduexi el titol del llibre")
        autor = input("Introduexi l'autor del llibre")
        rating = input("Introduexi la valoracio del llibre(1-5)")
        afegir = digitalbook(title, autor, rating)
        afegir.infoB(title, autor)
        afegir.rating(rating)
    def add_DBook(self):
        with open ("Informe_d'estat_de_la_biblioteca(Llibres_digitals).csv",'a', encoding="utf-8") as colecction_the_books:
            Colecction_books = csv.DictWriter(colecction_the_books, fieldnames=HEADER)
            Colecction_books.writerow(varD())
class Add_Phisic_BookInterface(logisitc_of_library):
    def add_Pbook(self):    
        title = input("Introduexi el titol del llibre")
        autor = input("Introduexi l'autor del llibre")
        state = input("Introduexi l'estat del llibre(llogat o no llogat)")
        phisical = input("Introduexi l'estat fisic del llibre")
        afegir = phisicalbook(title, autor, state, phisical)
        afegir.infoB(title, autor)
        afegir.state(state)
        afegir.phisic(phisical)
    def add_PBook(self):
        with open ("Informe_d'estat_de_la_biblioteca(Llibres_fisics).csv",'a', encoding="utf-8") as colecction_the_books:
            Colecction_books = csv.DictWriter(colecction_the_books, fieldnames=HEADER2)
            Colecction_books.writerow(varP())
class View_DigitalBooks_LibraryInterface(logisitc_of_library):
    def viewD(self):
        with open(FILE_NAME, "r", newline="")as csv_file:
            reader = list(csv.DictReader(csv_file))
            for i in reader:
                print(f"titol: {i[HEADER[0]]}")
                print(f"autor: {i[HEADER[1]]}")
                print(f"valoracio: {i[HEADER[2]]}")

class View_PhisicallBooks_LibraryInterface(logisitc_of_library):
    def viewP(self):
        with open(FILE_NAME2, "r", newline="")as csv_file:
            reader = list(csv.DictReader(csv_file))
            for i in reader:
                print(f"titol: {i[HEADER2[0]]}")
                print(f"autor: {i[HEADER2[1]]}")
                print(f"estat: {i[HEADER2[2]]}")
                print(f"estat fisic: {i[HEADER2[3]]}")

class AddRatingDigitalBookInterface(logisitc_of_library):
    def addDrating(self):
        selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))
        with open(FILE_NAME, "r", newline="") as csv_file:
                reader = list(csv.DictReader(csv_file))
                seleccion = reader[selected]
                act = {}
                print(f"Valoracio actual: {seleccion[HEADER[2]]}")
                act[HEADER[2]] = input("introdueix la nova valoracio: ")
                act[HEADER[0]] = seleccion[HEADER[0]]
                act[HEADER[1]] = seleccion[HEADER[1]]
                reader[selected] = act
                with open(FILE_NAME, mode="w", newline="", encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=HEADER)
                    writer.writeheader()
                    writer.writerows(reader)


class RentingPhisicalBookInterface(logisitc_of_library):
    def rent(self):
        with open(FILE_NAME2, "r", newline="") as csv_file:
            reader = list(csv.DictReader(csv_file))
            for row in reader:
                 print(" Aquest son tots els llibres fisics que hi ha " ,(row[HEADER2[0]]))
            selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))     
        
            reader = list(csv.DictReader(csv_file))
            seleccion = reader[selected]
            act = {}
            print(f"Estat actual: {seleccion[HEADER2[2]]}")
            act[HEADER2[2]] = input("introdueix el nou estat (Rentat o disponible): ")
            act[HEADER[0]] = seleccion[HEADER[0]]
            act[HEADER[1]] = seleccion[HEADER[1]]
            reader[selected] = act
            with open(FILE_NAME2, mode="w", newline="", encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=HEADER2)
                writer.writeheader()
                writer.writerows(reader)

class ViewPhisicalBookStateInterface(logisitc_of_library):
    def viewPP(self):
        with open(FILE_NAME2, "r", newline="", encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                print(" Aquest son tots els llibres fisics que hi ha " ,(row[HEADER2[0]]))
        selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))
        with open(FILE_NAME2, "r", newline="") as csv_file:
            reader = list(csv.DictReader(csv_file))
            seleccion = reader[selected]
            print(f"estat(rentat): {seleccion[HEADER2[2]]}")
            print(f"estat fisic: {seleccion[HEADER2[3]]}")
         


class ViewDigitalBookRatingInterface(logisitc_of_library):
    def viewDD(self):
        with open(FILE_NAME, "r", newline="", encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                print(" Aquest son tots els llibres digitals que hi ha " ,(row[HEADER2[0]]))
        selected = int(input("Quin vols seleccionar?: (has de escriure el numero amb l'ordre que ho has afegit el primer es el 0) "))
        with open(FILE_NAME, "r", newline="") as csv_file:
            reader = list(csv.DictReader(csv_file))
            seleccion = reader[selected]
            print(f"ultima valoracio: {seleccion[HEADER[2]]} estrelles")
                

while True:
    print("1 Afegir un llibre digital, 1.1 fisic")
    print("2 Veure tots els llibres i tota l'informacio d'un digital, 2.1 fisic")
    print("3 Cambiar una valoracio a un llibre")
    print("4 Llogar un llibre")
    print("5 Veure l'estat fisic i de disposicional d'un llibre")
    print("6 Veure valoracio d'un llibre")
    print("7 Sortir")
    print("8 Sortir i eliminar tots els llibres")
    print("""Recordeu: les valorqacions van de 1 a 5.
          Heu d'escriure els noms dels llibres tal cual com els heu afegit, es pot consultar al document.
            A la opcio 2/2.1 es mostraran tots els noms dels llibres i despres heu d eseleccionar una per veurer-ho complet
          Per fer feina sempre hi ha d'haber minim un llibre a cada document (digital i fisic)
          """)

    option = input("Quina opció vols?: ")


    if option == "1": #Bien
            add_digital_book = Add_Digital_BookInterface()
            add_digital_book.add_DBook()
    elif option == "1.1": #Bien
            add_phisical_book = Add_Phisic_BookInterface()
            add_phisical_book.add_PBook()
    elif option == "2": #Funciona
            view_digital = View_DigitalBooks_LibraryInterface()
            view_digital.viewD()
    elif option == '2.1': # Funciona
            view_fisica = View_PhisicallBooks_LibraryInterface()
            view_fisica.viewP()
    elif option == "3": #Bien
        change_rating = AddRatingDigitalBookInterface()
        change_rating.addDrating()
    elif option == "4": #Mal (Da error)
        rent = RentingPhisicalBookInterface()
        rent.rent()
    elif option == "5": #Bien
        view_phisic = ViewPhisicalBookStateInterface()
        view_phisic.viewPP()
    elif option == "6": #Bien
        view_rating = ViewDigitalBookRatingInterface()
        view_rating.viewDD()
    elif option == "7":
        print("Sortinit de la biblioteca, GRACIES !!!")
        break
    elif option == "8":
        print("ELIMINANT INFORME")
        print("Sortinit de la biblioteca, GRACIES !!!")
        os.remove("Informe_d'estat_de_la_biblioteca(Llibres_digitals).csv")
        os.remove("Informe_d'estat_de_la_biblioteca(Llibres_fisics).csv")
        break
    else:
        print('no existeixa una opcio amb aquest nombre, introdueix un altre per favor.')


#Bien--Funciona como toca
#Funciona--Hace lo que pide el enunciado pero no fuciona como se supone que he programado
#Mal--No funciona como toca