"""
exercici: crea un sistema de notificacions

requisits:
    -Els sistema pot enviar Email, Push i SMS (implementacions especifiques).
    -El sistema no pot dependre de les implementacions especifiques.

instruccions:
    -Crear interficie o classe abstracta
    -Fer les implementacions especifiques
    -Crear un sistema de notificacions utilitzant DIP i comprova que es compleix
"""

from abc import ABC, abstractmethod

class NotifierInterface(ABC):
    @abstractmethod
    def send(self, message):
        pass


class Email(NotifierInterface):
    def send(self, menssage):
        print(" s'ha enviat per Email el missatge ", menssage)

class Push(NotifierInterface):
    def send(self, menssage):
        print(" s'ha enviat per Push el missatge ", menssage)

class SMS(NotifierInterface):
    def send(self, menssage):
        print(" s'ha enviat per SMS el missatge ", menssage)

class NotificationService:
    def __init__(self, notifier:NotifierInterface):
        self.notifier = notifier

    def notify(self, menssage):
        self.notifier.send(menssage)


noti_1 = NotificationService(Email())
noti_1.notify("Buenos dias chat")

noti_2 = NotificationService(SMS())
noti_2.notify("Momento incomodo")