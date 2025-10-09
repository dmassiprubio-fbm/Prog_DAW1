# INCORRECTE

# class User:

#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def save_to_database(self):
#         print('Guardando en BD')

#     def sned_email(self, message):
#         print(f"S'ha mandat el correu amb missatge: {message}")


# CORRECTE 

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

class EmailInterface:

    def send_email(self, message):
        print(f"S'ha mandat el correu amb missatge: {message}")

class DB_Interface:

    def save_to_database(self, user: User):
        print('Guardando en BD')

# Exemple

class Superhero:
    def __init__(self, name):
        self.name = name
    
    def prtform_super_skill(self):
        pass



    # def fly(self):
    #     print('Está volando')

    # def ray_x(self):
    #     print('Está disparando rayos!')

    # def super_speed(self):
    #     print("Está corriendo a super volando!")