"""
Exercici: 
Crar un gestor de impresora:

requisits:
    -Tenim impressores en blanc i negre
    -Impressores a color
    -Impressores multifunció (imprimir, escanejar i enviar correus).
Instruccions:
    -Implementar un sistema, amb els diferents tipos d'impressores i funcions.
    -Aplicar el principi ISP
    -Comprovar que es compleix el principi.
"""

from abc import ABC, abstractmethod

class InterfaceBlncINegre(ABC):
    @abstractmethod
    def imprimirbn(self):
        pass

class InterfaceColor(ABC):
    @abstractmethod
    def imprimircolor(self):
        pass

class Interfaceescanetjar(ABC):
    @abstractmethod
    def escanetjar(self):
        pass

class Interfaceenviar(ABC):
    @abstractmethod
    def enviar_correus(self):
        pass

class impresoraBN(InterfaceBlncINegre):
    def imprimirbn(self):
        print('Imprimeix en blanc i negre')

class impresoracolor(InterfaceColor):
    def imprimircolor(self):
        print('Imprimeix a color')

class imporesoramulti(InterfaceColor, Interfaceescanetjar, Interfaceenviar):
    def imprimircolor(self):
        print('Imprimeix a color')
    
    def enviar_correus(self):
        print('Envia correus')

    def escanetjar(self):
        print('escanetja documents')


color = impresoracolor()
bn = impresoracolor()
multi = imporesoramulti()


print('la impresora b i n ', bn)
print('la impresora a color ', color)
print('la impresora multifuncions ', multi)
