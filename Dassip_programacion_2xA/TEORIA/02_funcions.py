"""
1️⃣Crea exemples de funcions bàsiques que representin les diferents possibilitats del llenguatge:

    Sense paràmetres ni retorn, amb un o diversos paràmetres, amb retorn...
    Comprova si pots crear funcions dins de funcions.

2️⃣Utilitza algun exemple de funcions ja creades en el llenguatge.
3️⃣Posa a prova el concepte de variable LOCAL i GLOBAL.
4️⃣Has de fer print per consola del resultat de tots els exemples.

DIFICULTAT EXTRA (Puntua si el resols totsol):
5️⃣Crea una funció que rebi dos paràmetres de tipus cadena de text i retorni un número. La funció imprimeix tots els números de l'1 al 100. Tenint en compte que:

    Si el número és múltiple de 3, mostra la cadena de text del primer paràmetre.
    Si el número és múltiple de 5, mostra la cadena de text del segon paràmetre.
    Si el número és múltiple de 3 i de 5, mostra les dues cadenes de text concatenades.
    La funció retorna el nombre de vegades que s'ha imprès el número en lloc dels textos.
"""

###Simple###

def greet():
    print('hola')

greet()

###Amb retorn###

def return_greet():
    return 'hola pum pum pum pum, carmanyoooola'

print(return_greet())

###Amb un parametre###

def arg_greet(name):
    print(f'hola, cual es este pokemon, este pokemon es... {name}')

arg_greet('macaco david')

###Amb mès d'un parametre###

def args_greet(greet, name):
    print(f'{greet}, {name}')

args_greet('pum pum pum pum ', 'Carmanyoooooola')

###Amb parametre opcional###

def  opcional_greet(name='Alumne'):
    print(f'hola carmanyola, {name}')

opcional_greet()
opcional_greet('Carlos')


def opcional_greet_2(greet, name='Alumne'):
    print(f'{greet}, {name}')

opcional_greet_2('hola caracola')
opcional_greet_2('hola', name='Carlitos')

###Amb divesos return

def multi_return_greet():
    return 'hola caracola', 'Carlitos'

multi_return_greet()

def multi_return_grert_2():
    greet = 'Hola'
    name = 'Carlos'
    return (greet, name)

print(multi_return_grert_2())
my_greet, my_name = multi_return_grert_2()
print(my_greet)
print(my_name)

###Amb un numero infinits d'arguments###
def variable_arg_sum(*nums):
    sum = 0
    for num in nums:
        sum += num
    print(f'la suma de tots és: {sum}')

variable_arg_sum()

variable_arg_sum(3,2)

variable_arg_sum(2,58,258,5,85,6,21,85,51,5,6,4,14,5,55621,852,415,14,4,8521,74,54,548,41,17,97,4568,41,8574,86,74,841,84,389,4,98,74168,74,6874864,8,489,64,874,68,74,68,714,87,59,749,867)

###Amb un numero variable d'argumenrs amb clau###

def variable_key_arg_func(**kargs):
    for kay, value in kargs.items():
        print(f'{kay}: {value}')

variable_key_arg_func(name = 'damian', surname = 'massip', age = 17)
