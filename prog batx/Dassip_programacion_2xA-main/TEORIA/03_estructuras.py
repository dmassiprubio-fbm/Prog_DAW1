"""
1️⃣Mostra exemples de creació de totes les estructures suportades per defecte a Python.
Utilitza operacions d'inserció, esborrament, actualització i ordenació.
DIFICULTAT EXTRA (Puntua si el resols totsol):
2️⃣Crea una agenda de contactes per terminal.
Has d'implementar funcionalitats de cerca, inserció, actualització i eliminació de contactes.
Cada contacte ha de tenir un nom i un número de telèfon.
El programa sol·licita, en primer lloc, quina és l'operació que es vol realitzar, i a continuació les dades necessàries per a dur-la a terme.
El programa no pot deixar introduir números de telèfon no numèrics i amb més d'11 dígits (o el nombre de dígits que vulguis).
També s'ha de proposar una operació de finalització del programa.
"""

"""
ESTRUCURES
"""

# Llistes
my_list = ["Guillem", "Daniel", "Carlos", "Alba"]
print(my_list)


# Afegir
my_list.append("Damià")
my_list.append("Damià")
print(my_list)


# Eliminar
my_list.remove("Carlos")
print(my_list)
my_list.remove("Damià")


# Accès
print(my_list[1]) # Segona posició


# Actalització
my_list[1] = "Iker"
print(my_list)


# Ordenar
my_list.sort
print(my_list)
my_list.reverse
print(my_list)


# Afegir a una Posició 
my_list.insert(2, "Carlos")
print(my_list)


"""
TUPLES
"""

my_tuple = ("Guillem", "Mas", "36", "@guillemmas")
#Acces
print(my_tuple[0])
my_tuple = tuple(sorted(my_tuple)) #si ordenam en converteix en llista !!!
print(my_tuple)
print(type(my_tuple))

'''
Set
'''

my_set = {'Guillem', 'Mas', '@guillemmas', '36'}
print(my_set)
my_set.add('gmas@iessarenal.net')
print(my_set)
my_set.add('gmas@iessarenal.net') #Si ja existeix un element no l'afegirà
print(my_set)
my_set.remove('Guillem')
print(my_set)

'''
Diccionaria
'''

my_dic = {'name':'Guillem', 
          'Surname':'Mas', 
          'Age':'36', 
          'Alias':'@guillemmas'
          }
print(my_dic)
my_dic['email'] = 'gmas@iessarenal.net' #afegir
print(my_dic)

my_dic['Surname'] = 'MAS MAS' #ACTUALITZAR
print(my_dic)

del my_dic['Surname'] #Eliminar
print(my_dic)

'''
2️⃣Crea una agenda de contactes per terminal.
Has d'implementar funcionalitats de cerca, inserció, actualització i eliminació de contactes.
Cada contacte ha de tenir un nom i un número de telèfon.
El programa sol·licita, en primer lloc, quina és l'operació que es vol realitzar, i a continuació les dades necessàries per a dur-la a terme.
El programa no pot deixar introduir números de telèfon no numèrics i amb més d'11 dígits (o el nombre de dígits que vulguis).
També s'ha de proposar una operació de finalització del programa.
'''



def agenda():
    
    agenda = {} #Diccionari buit: 

    def insert_phone(): #funcio interna dins la funció agenda
        phone = input('introdueix el numero de telefon:  ')
        if len(phone) > 0 and len(phone) <= 11 and phone.isdigit():
            agenda[name] = phone



    while True:
        print('')
        print('1.Cercar contacte')
        print('2.Afegir contacte')
        print('3.Actualitzar contacte')
        print('4.Eliminar contcte')
        print('5.Sortir')

        option = input('Selecciona una opcio ')
        if (option == '1'):
            name = input('introdueix el nom del contacte:  ')
            if name in agenda: #comprovar si existeix la clau dins el diccionari
                print(agenda[name])
            else:
                print('no existeix el contacte')
        elif (option == '2'):
            name = input('indrodueix el nom del contacte:  ')
            insert_phone()
        elif (option == '3'):
            name = input('indrodueix el nom del contacte:  ')
            if name in agenda:
                    insert_phone()
            else:
                print('no existeix el contacte')
        elif (option == '4'):
            name = input('indrodueix el nom del contacte:  ')
            if name in agenda:
                del agenda[name]
            else:
                print('no existeix el contacte')
        elif (option == '5'):
            print('sortint de la agenda')
            break
        else:
            print('selecciona una opcio correcta')

agenda()