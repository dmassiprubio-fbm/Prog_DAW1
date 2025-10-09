'''
DIFICULTAT EXTRA (Puntua si el resols totsol):
4️⃣ Crea una funció que sigui capaç de processar paràmetres, però que també pugui llançar 3 tipus diferents d'excepcions 
(una d'elles ha de correspondre's amb una mena d'excepció creada per nosaltres de manera personalitzada, i ha de ser llançada de manera manual)
en cas d'error.
-longitud < 3
-segon element/posició [1] no pot ser 0
-quart element ha de ser str
5️⃣ Captura totes les excepcions des del lloc on anomenes a la funció.
6️⃣ Imprimeix el tipus d'error.
7️⃣ Imprimeix si no s'ha produït cap error.
8️⃣ Imprimeix que l'execució ha finalitzat.
'''


'''
lista = [2,3,4,5,6]
class Errorerror(Exception):
    pass
if len(lista) < 3:
    raise Errorerror ('la longitud es major que 3')
elif lista[1] == 0:
    raise Errorerror ('el segon caracter es 0')
'''



class ErrorTonto(Exception):
    pass
'''
while True:
    num_a = (input('introdueix un numero:  '))
    num_b = (input('introdueix un altra numero:  '))
    if(num_a + num_b == 'DAVIDEULOGIO'):
        raise ErrorTonto('este es un mindundi, no lo quiero en mi programa')
'''

def proces_params(parameters: list):
    print(type(parameters[3]))
    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[3]) != str:
        raise ErrorTonto("aaaa")
    
lista = [1,5,5,5]

try:
    proces_params(lista)
except IndexError as e:
    print("el nombre d'elements ha de ser major a 3")
except ZeroDivisionError as e:
    print('el segon parametre de la llista no pot ser 0')
except ErrorTonto as e:
    print(e)
else:
    print('no hi ha cap error')