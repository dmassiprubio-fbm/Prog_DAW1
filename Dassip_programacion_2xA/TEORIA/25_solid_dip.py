#Incorrecte 

# class Switch:
#     def turn_on(self):
#         print('Encendre lampara')

#     def turn_off(self):
#         print('Aturar lampara')
    
# class Lamp:
#     def __init__(self):
#         self.switch = Switch()

#     def operate(self,command):
#         if command == 'on':
#             self.switch.turn_on()
#         else:
#             self.switch.turn_off()

# lampara =  Lamp()
# lampara.operate('on')
# lampara.operate('off')

from abc import ABC, abstractmethod

class SwitchInterface(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class ClassicSwitch(SwitchInterface):
    def turn_on(self):
         print('Encendre lampara')

    def turn_off(self):
         print('Aturar lampara')

class AutomaticSwitch(SwitchInterface):
    def turn_on(self):
         print("es detecta moviment, s'atura")

    def turn_off(self):
         print("A passat cert temps, s'atura")

class Lamp:
    def __init__(self, switch:SwitchInterface):
        self.switch = switch

    def operate(self, command):
        if command == "on":
            self.switch.turn_on
        else:
            self.switch.turn_off

lamp_1 = Lamp(ClassicSwitch())
lamp_1.operate("ON")

lamp_2 = Lamp(AutomaticSwitch())
lamp_2.operate("ON")