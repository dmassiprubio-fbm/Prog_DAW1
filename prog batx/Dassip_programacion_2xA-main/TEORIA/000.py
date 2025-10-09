'''
tipos de datos  
operadores  +
funciones- parametros de entrada +
funciones- return +
listas
sets
tuplas
dict
clases- herencia
clases- polimorfismoi
'''

'''
listas:
añadir elementos: .append()
eliminar elementos: .remove()
acceso a elementos: [posicion]
actualizar elementos: [posicion] = nuevo_valor
ordenar elementos: .sort()
ordenar elementos: .reverse()
añadir elementos en una posicion: .insert(posicion, nuevo_valor)
'''
'''
tuplas:
acceso a elementos: [posicion]
ordenar elementos: sorted(), pero se convierte en lista
'''
'''
sets:
es con {}
añadir elementos: .add(), si esta repetido no lo añade
eliminar elementos: .remove()
'''
'''
diccionarios:
es con {}
añadir elementos: [clave] = valor
eliminar elementos: del dic[clave]
actualizar elementos: [clave] = nuevo_valor
'''

'''
clases:
class nombre_clase:
    def __init__(self, parametros):
        self.parametros = parametros
    def nombre_funcion(self):
        return self.parametros

class nombre_clase_hija(nombre_clase):
    def __init__(self, parametros):
        super().__init__(parametros)
    def nombre_funcion(self):
        return self.parametros

class nombre_clase2(ABC):
    @abstractmethod
    def nombre_funcion(self):
        pass
        
class nombre_clase_hija2(nombre_clase2):
    def nombre_funcion(self):
        return self.parametros
'''