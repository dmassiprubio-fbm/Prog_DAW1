#simpre la misma estructura

class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance



singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1)
print(singleton2)

class UserSession:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance
    
    def set_user(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def clear_user(self):
        self.id = None
        self.nombre = None


    def get_user(self):
        print(f"{self.id} - {self.nombre}")

session1 = UserSession()
session1.set_user("1", "Damian")

session1.get_user()

session2 = UserSession()
session2.get_user()
session2.set_user("1", " RT_Dromus5000-_-")
session2.get_user()

session1.get_user()