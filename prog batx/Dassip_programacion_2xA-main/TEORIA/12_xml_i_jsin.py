'''
1️⃣ Desenvolupa un programa capaç de crear un arxiu XML i JSON que guardi les següents dades (fent ús de la sintaxi correcta en cada cas):

    Nom
    Edat
    Data de naixement
    Llistat de llenguatges de programació

2️⃣ Mostra el contingut dels arxius.
3️⃣ Esborra els arxius.

DIFICULTAT EXTRA (Puntua si el resols totsol):
4️⃣ Utilitzant la lògica de creació dels arxius anteriors, crea un programa capaç de llegir i transformar en una mateixa classe del teu llenguatge les dades emmagatzemades en l'XML i el JSON.
'''

data = {
    'name' : 'Damia Massip',
    'age' : 17,
    'birth_date' : '24-05-07',
    'programing_languages' : ['Python', 'Psint', 'Java']
}

with open('fitxer.txt', 'w') as file:
    for k, v in data.items(): #k sa part de devant i la v el valor de cada una, son per recorrer el diccionari
        file.write(f'{k}:{v}\n')

### XML ###

import xml.etree.ElementTree as xml

root = xml.Element('data')
for k, v in data.items():
    child = xml.SubElement(root, k)
    if isinstance(v, list):
        for item in v:
            xml.SubElement(child, 'item').text = item
    else:
        child.text = str(v)

tree = xml.ElementTree(root)
tree.write('fitxer.xml')

with open('fitxer.xml', 'r') as xml_file:
    root = xml.fromstring(xml_file.read())
    print(root.find('age').text)
    print(root.find('name').text)

#JSON

import json 

with open('fitxer.json', 'w') as json_file:
    json.dump(data, json_file)

with open('fitxer.json', 'r') as json_file:
    #print(json_file.read())
    json_dic = json.load(json_file)
    print(json_dic['age'])
    print(json_dic['name'])