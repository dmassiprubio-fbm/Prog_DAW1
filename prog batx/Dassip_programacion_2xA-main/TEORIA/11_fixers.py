'''
1️⃣ Desenvolupa un programa capaç de crear un arxiu amb el teu nom i tingui l'extensió .txt.
2️⃣ Afegeix diverses línies en aquest fitxer:

    El teu nom.
    Edat.
    Llenguatge de programació favorit.

3️⃣ Imprimeix el contingut.
4️⃣ Esborra el fitxer.

DIFICULTAT EXTRA (Puntua si el resols totsol):

5️⃣ Desenvolupa un programa de gestió de vendes que emmagatzema les seves dades en un arxiu .txt.
6️⃣ Cada producte es guarda en una línia de l'arxiu de la manera següent:

    [nom_producte], [quantitat_venuda], [preu].
    Seguint aquest format, i mitjançant terminal, ha de permetre afegir, consultar, actualitzar, eliminar productes i sortir.
    També ha d'haver-hi opcions per a calcular la venda total i per producte.
    L'opció sortir esborra el .txt.
'''

import os

###Fixers##

#open('damia.txt','w') open pero obrior i/o crear un fitxer
#os.remove('damia.txt') eliminar l'arxiu

with open('damia.txt','a') as file: #utilitzarem el whit, per que no es pugui modificar res.
    file.write('Damia Massip\n')
    file.write('17\n')
    file.write('PSint')

    

with open('damia.txt','r') as file:
    print(file.read())

with open('damia.txt','r') as file:
    print(file.readline())

with open('damia.txt','r') as file:
    for line in file.readlines():
        print(line)

os. remove('damia.txt')
