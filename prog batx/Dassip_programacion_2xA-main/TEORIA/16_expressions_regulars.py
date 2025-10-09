'''
1️⃣ Explora el concepte d'expressions regulars, creant una funció capaç de trobar i extreure tots els nombres d'un text.

DIFICULTAT EXTRA (Puntua si el resols tot sol):

2️⃣ Crea 3 expressions regulars capaces de:
    - Validar un email.
    - Validar un número de telèfon.
    - Validar un URL.
'''

import re

regexr = r"\d+"

def find_number(text):
    return re.findall(regexr,text)

print(find_number('Hola sóc alumne de 2n de Batxillerat del curs 2024'))

regexr = r"^\w+@[a-z]+.[a-z]{2,5}$"
def proto_find_email(text:str):
    return bool(re.match(regexr,text.lower()))

print(proto_find_email('dmassip@iessarenal.net'))
print(proto_find_email('dmasssip#iessarenal.net'))
print(proto_find_email('dmassip@iessarenal.GOOGLE'))

regexr = r"^\+?[\s\d]{2,}$"

def proto_find_numero(num: int):
    return bool(re.match(regexr, num))

print(proto_find_numero('649 79 10 70'))
print(proto_find_numero('+34 649 79 70 70'))
print(proto_find_numero('649791070')) 

regexr = r"http(s)?://(www.)?[\w.]+.[a-z]{2,}(/[\S]+)?"

def proto_fing_url(url):
    return bool(re.match(regexr, url))

print(proto_fing_url('https://classroom.google.com/c/Njk3NDU1MTQ2NDAx/a/NzM5Nzg3NjM0Nzk5/details'))