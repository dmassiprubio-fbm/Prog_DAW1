class vheicle:
    def __init__(self, brand:str, colour:str):
        self.brand = brand
        self.colour = colour
    
class Car(vheicle):
    def num_wheels(self):
        print('Un cotxe té 4 rodes')

class Motorbike(vheicle):
    def num_wheels(self):
        print('Un cotxe té 4 rodes')

class Boat(vheicle):
    def num_wheels(self):
        print('Un cotxe té 4 rodes')

my_car = Car('Toyota', 'Lila')
my_moto = Motorbike('Kawasaki','Lima')
my_boat = Boat('Titanic', 'Rojo')