'''
1️⃣ Explora el concepte d'herència segons Python. Crea un exemple que implementi una superclasse Animal i un parell de subclasses Ca i Moix, juntament amb una funció que serveixi per a imprimir el so que emet cada Animal.

DIFICULTAT EXTRA (Puntua si el resols totsol):
2️⃣ Implementa la jerarquia d'una empresa de desenvolupament formada per Empleats que poden ser Gerents, Gerents de Projectes o Programadors.
3️⃣ Cada empleat té un identificador i un nom.
4️⃣ Depenent de la seva labor, tenen propietats i funcions exclusives de la seva activitat, i emmagatzemen els empleats a càrrec seu.
'''

#superclase

class Animal:
    def __init__(self, name:str , color:str) -> None:
        self.name = name
        self.color = color

    def sound(self):
        print('sonido no especificado')

#sublases
class Dog(Animal):
    def sound(self):
        print('Guau Guau !!')
class Cat(Animal):
    def sound(self):
        print('Miau !!')
class Bird(Animal):
    def sound(self):
        print('Pio Pio !!')



def print_sound(animal:Animal):
    animal.sound()

perro = Dog('Perro','Negro')
gato =  Cat('Gato','Blanco')
pajaro = Bird('pajaro', 'amarillo')


print_sound(perro)
print_sound(gato)
print_sound(pajaro)


'''
DIFICULTAT EXTRA (Puntua si el resols totsol):
2️⃣ Implementa la jerarquia d'una empresa de desenvolupament formada per Empleats que poden ser Gerents, Gerents de Projectes o Programadors.
3️⃣ Cada empleat té un identificador i un nom.
4️⃣ Depenent de la seva labor, tenen propietats i funcions exclusives de la seva activitat, i emmagatzemen els empleats a càrrec seu.
'''

class Empleat:
    def __init__(self, nom:str, identificador:int) -> None:
        self.nom = nom
        self.identificador = identificador

    def propietats_funcions(self):
        print('no te propietats ni funcions especifiques')

class Gerent(Empleat):
    def coodinate_project(self):
        print(f"{self.nom} coordina tots els projectes")

class Gerent_projectos(Empleat):
    def __init__(self, nom:str, identificador:int, proyect:str) -> None:
        super().__init__(nom, identificador)
        self.proyect = proyect

    def coodinate_project(self):
        print(f"{self.nom} coordina {self.proyect}")

class Programador(Empleat):
    def __init__(self, nom:str, identificador:int, language:str) -> None:
        super().__init__(nom, identificador)
        self.language = language
        
    def code(self):
        print(f"{self.nom} esta programant en {self.language}")


gerent = Gerent('Damia','1')
gerente_p_1 = Gerent_projectos('Carlos','2','minecraft 2')
gerente_p_2 = Gerent_projectos('Guillem','3','hackear el pentagono')
programador_1 = Programador('Mati', '4', 'c++')
programador_2 = Programador('Alba', '5','java')
programador_3 = Programador('Houssam', '6', 'Python')
programador_4 = Programador('Eulogio', '7', 'PSint')


programador_1.code()
programador_4.code()
gerent.coodinate_project()
gerente_p_1.coodinate_project()

