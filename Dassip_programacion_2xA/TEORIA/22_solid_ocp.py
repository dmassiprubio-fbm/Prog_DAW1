#  INCORRECTE

# class From:
#     def draw(self):
#         print('Dibuixar un quadrat!')

#     def draw_circle(self):
#         print('Dibuixar un cercle')

from abc import ABC, abstractmethod

class From(ABC):

    @abstractmethod
    def draw(self):
        pass

class Square(From):
    def draw(self):
        print('dibuixa un quadrat!')

class Cercle(From):
    def draw(self):
        print('dibuixa un cercle!')

    
"""
Desenvolupar una calculadora que permeti desenvolpupar diferents operacions
Primera part: implementar suma, resta, mult i div
segona part: implementar potències
"""

class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class Suma(Operation):
    
    def execute(self, a, b):
        return a + b

class Resta(Operation):
    
    def execute(self, a, b):
        return a - b
    
class Mult(Operation):
    
    def execute(self, a, b):
        return a * b
    
class Div(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError()
        return a / b
    
class Pot(Operation):

    def execute(self, a, b):
        return a ** b

class Calculator:
    def __init__(self):
        self.operations = {}

    def add_operation(self, name, operation):
        self.operations[name] = operation

    def calculate(self, op, a, b):
        return self.operations[op].execute(a, b)

    

calculator = Calculator()
calculator.add_operation('Mi Suma', Suma())
calculator.add_operation('Mi Resta', Resta())
calculator.add_operation('Mi Potencia',Pot())
calculator.add_operation('Mi Division',Div())

print(calculator.calculate("Mi Suma", 3, 4))
print(calculator.calculate("Mi Division", 3, 0))