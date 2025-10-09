'''
import csv

# Definir los campos (nombres de columna)
campos = ['Nombre', 'Edad', 'Ciudad']

# Abrir el archivo CSV en modo escritura
with open('nuevo_archivo.csv', mode='w', newline='', encoding='utf-8') as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    
    # Escribir el encabezado (nombres de columna)
    escritor.writeheader()

    # Pedir al usuario que ingrese datos
    while True:
        # Solicitar datos al usuario
        nombre = input("Introduce el nombre: ")
        edad = input("Introduce la edad: ")
        ciudad = input("Introduce la ciudad: ")

        # Crear un diccionario con los datos introducidos
        fila = {'Nombre': nombre, 'Edad': edad, 'Ciudad': ciudad}
        
        # Escribir la fila en el archivo CSV
        escritor.writerow(fila)

        # Preguntar si el usuario desea agregar más datos
        continuar = input("¿Quieres agregar otra persona? (s/n): ")
        if continuar.lower() != 's':
            break

print("Datos guardados en 'nuevo_archivo.csv'.")
'''



'''
def one():
        name = str(input('introdueix el nom del joc '))
        time = int(input('introdueix el temps de duracio del joc '))
        price = int(input('introdueix el preu del joc '))
        age = int(input('introdueix la edat minima recomenada per jugar al joc '))
        genre = str(input('introdueix el genere del joc '))
        dict_head = {
        }
        header = ['nom', 'temps', 'peru', 'edat', 'genere']
        return dict_head
'''


'''
with open ('Coleccio_jocs.csv','a', encoding='utf-8') as colecction_the_games:
            Colecction_games = csv.writer(colecction_the_games, delimiter=',')
            Colecction_games.writerow(one())
'''
import csv
import os
import time


FILE_NAME = "comics.csv"
FIELDNAMES = ["comic", "release_date", "colection", "readed"]

def init_file():
    if not os.path.isfile(FILE_NAME):
       with open(FILE_NAME, "w", newline="") as csv_file:           
            writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
            writer.writeheader()
           

def add_comic():
    with open(FILE_NAME, "a", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
        new_comic = {
            FIELDNAMES[0]:input("Introdueix el nom del còmic: "),
            FIELDNAMES[1]:input("Introdueix la data de publicació (dd/mm/yyyy): "),
            FIELDNAMES[2]:input("Introdueix la col·lecció: "),
            FIELDNAMES[3]: False,
        }
        writer.writerow(new_comic)      

def render_csv_search_options():
    with open(FILE_NAME, "r", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for index, row in enumerate(reader):
            print(f"{index}: {row[FIELDNAMES[0]]}")

def view_comic():
    render_csv_search_options()
    selected = int(input("Quin vols seleccionar? (Selecciona el número): "))
    with open(FILE_NAME, "r", newline="") as csv_file:
        reader = list(csv.DictReader(csv_file))
        selected_option = reader[selected]
        print(f"Títol: {selected_option[FIELDNAMES[0]]}")
        print(f"Data sortida: {selected_option[FIELDNAMES[1]]}")
        print(f"Col·lecció: {selected_option[FIELDNAMES[2]]}")
        print(f"Llegit: {selected_option[FIELDNAMES[3]]}")
        print("\n\n")     

def edit_comic():
    render_csv_search_options()
    selected = int(input("Quin vols modificar? (Selecciona el número): "))
    with open(FILE_NAME, "r", newline="") as csv_file:
        reader = list(csv.DictReader(csv_file))
        selected_option = reader[selected]
        new_comic = {}
        print(f"Títol actual: {selected_option[FIELDNAMES[0]]}")
        new_comic[FIELDNAMES[0]] = input("Introdueix el nom nou del còmic: ")
        print(f"Data sortida: {selected_option[FIELDNAMES[1]]}")
        new_comic[FIELDNAMES[1]] = input("Introdueix la data nova de publicació (dd/mm/yyyy): ")
        print(f"Col·lecció: {selected_option[FIELDNAMES[2]]}")
        new_comic[FIELDNAMES[2]] = input("Introdueix la nova col·lecció: ")
        new_comic[FIELDNAMES[3]] = selected_option[FIELDNAMES[3]]
        print("\n\n")  
        reader[selected] = new_comic
    with open(FILE_NAME, mode='w', newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(reader)

def menu():
    print("MENU COL·LECCIÓ COMICS")
    print("1 - Afegir")
    print("2 - Consultar")
    print("3 - Modificar")
    print("4 - Eliminar")
    print("0 - Sortir")
    op = int(input("Selecciona una opció: "))
    while op != 0:  
        os.system("clear")     
        if op == 1:
            add_comic()
        elif op == 2:
            view_comic()
        elif op == 3:
            edit_comic()
        elif op == 4:
            pass           
        
        print("MENU COL·LECCIÓ COMICS")
        print("1 - Afegir")
        print("2 - Consultat")
        print("3 - Modificar")
        print("4 - Eliminar")
        print("0 - Sortir")
        op = int(input("Selecciona una opció: "))
    else:
        print("Sortint...")
        time.sleep(3)



init_file()
menu()    