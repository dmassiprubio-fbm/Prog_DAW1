'''
1️⃣ Explora el concepte de maneig d'excepcions de Python.
2️⃣ Força un error en el teu codi, captura l'error, imprimeix aquest error i evita que el programa es detingui de manera inesperada.
3️⃣ Prova de dividir "10/0" o accedir a un índex no existent d'un llistat per a intentar provocar un error.

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
result = 0
try:
    result = 10/0
except Exception as e:
    print(f"S'ha produït un error: {e} ({type(e).__name__})")

print(result)

# Errors propis

class ErrorTonto(Exception):
    pass
while True:
    num_a = (input('introdueix un numero:  '))
    num_b = (input('introdueix un altra numero:  '))
    if(num_a + num_b == 'DAVIDEULOGIO'):
        raise ErrorTonto('este es un mindundi, no lo quiero en mi programa')





