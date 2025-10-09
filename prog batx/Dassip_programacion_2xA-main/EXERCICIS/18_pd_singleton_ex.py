"""

    - Afegir producte
    - Eliminar producto
    - Pagar -> Borrarà tots els elements
"""

class CarritoCompra:
    products_list = []
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(CarritoCompra, cls).__new__(cls)
        return cls._instance

    def show_menu():
        print('1 Afegir producte')
        print('2 Elimnar producte')
        print('3 Pagar tot')

    def add_product(self, name):
        self.products_list.append(name)
    
    def del_product(self, name):
        self.products_list.remove(name)

    def pay(self):
        self.products_list.clear()

    op = input('selecciona un apartat del menu')

    if op == '1':
        add_product()
    elif op == '2':
        del_product
    elif op == '3':
        pay