# Incorrrecte

from abc import ABC, abstractmethod

# class WorkerInterface(ABC):
#     @abstractmethod
#     def work(self):
#         pass

#     @abstractmethod
#     def eat(self):
#         pass

# class human(WorkerInterface):
#     def work(self):
#         print('Treballant')
#     def eat(self):
#         print('comer')

# class robot(WorkerInterface):
#     def work(self):
#         print('treballant')
    
#     def eat(self):
#         pass
#         #els robots no menjen

class WorkerInterface(ABC):
    @abstractmethod
    def work(self):
        pass

class EatInterface(ABC):
    @abstractmethod
    def eat(self): 
        pass

class Robot(WorkerInterface):
    def work(self):
        print('Treballant')

class Human(WorkerInterface, EatInterface):
    def work(self):
        print('Treballar')

    def eat(self):
        print('Menjant')
        

