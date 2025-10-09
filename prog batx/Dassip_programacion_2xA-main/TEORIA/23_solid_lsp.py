# Incorrecte

# class Bird:
#     def fly(self):
#         print("Flying!!")

# class Chicken(Bird):
#     def fly(self):
#         raise Exception("Les gallines no volen!!!")
    
# bird = Bird()
# bird.fly()

# chicken = Chicken()
# chicken.fly

class Bird:
    def move(self):
        print(" Està en moviment")

class Chicken(Bird):
    def move(self):
        print("Està caminant!")

class Pigeot(Bird):
    def move(self):
        print(" Està volant !!")

ocell = Bird()
ocell.move()
gallina = Chicken()
gallina.move()
pidgey = Pigeot()
pidgey.move()