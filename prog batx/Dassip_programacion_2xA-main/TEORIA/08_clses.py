'''
1️⃣ Explora el concepte de classe i crea un exemple que implementi un inicialitzador, atributs i una funció que els imprimeixi (tenint en compte les possibilitats del llenguatge).
2️⃣ Una vegada implementada, crea-la, estableix els seus paràmetres, modifica'ls i imprimeix-los utilitzant la seva funció.

DIFICULTAT EXTRA (Puntua si el resols totsol):
3️⃣Implementa dues classes que representin les estructures de Pila i Cua (estudiades en l'apartat 07 de la ruta d'estudi)

    Han de poder inicialitzar-se i disposar d'operacions per a afegir, eliminar, retornar el nombre d'elements i imprimir tot el seu contingut.
'''

class Programmer:

    nivel:str = "Novato"
    def __init__(self, name:str, age:int, lenguages:list):
        self.name = name
        self.age = age
        self.lenguages= lenguages

    def __str__(self) -> str:
        return f"Nom: {self.name} \n\t Edat: {self.age} \n\t Llenguatge: {self.lenguages} \n\t Nivell: {self.nivel}" # \n -> salto de linia | \n\t -> salto de linia + tabulado

my_programmer = Programmer("Guillem", 36, ["Python", "Java", "C++"])
my_programmer.age = 37
my_programmer.nivel = "Experto"
#print(my_programmer.name)
#print(my_programmer.lenguages, my_programmer.nivel)
print(my_programmer)