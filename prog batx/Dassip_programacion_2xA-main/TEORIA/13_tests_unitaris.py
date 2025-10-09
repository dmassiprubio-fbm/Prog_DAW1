"""
1️⃣ Crea una funció que s'encarregui de sumar dos números i retornar el seu resultat.
2️⃣ Crea un test, utilitzant les eines de Python, que sigui capaç de determinar si aquesta funció s'executa correctament.

DIFICULTAT EXTRA (Puntua si el resols totsol):
3️⃣ Crea un diccionari amb les següents claus i valors:
"name": "El teu nom"
"age": "La teva edat"
"birth_date": "La teva data de naixement"
 "programming_languages": ["Llistat de llenguatges de programació"]
4️⃣ Crea dos test:
Un primer que determini que existeixen tots els camps.
Un segon que determini que les dades introduïdes són correctes.
"""

import unittest

class Testsum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(2, 3), 5)
        self.assertEqual(sum(2, 1), 3)
        self.assertEqual(sum(-2, 3), 1)
        self.assertEqual(sum(-2, -3), -5)
        self.assertEqual(sum(0, 3), 3)
        
    
    
    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum('a', 4)
        with self.assertRaises(ValueError):
            sum( 4, '4')
        with self.assertRaises(ValueError):
            sum('a', '4')
        with self.assertRaises(ValueError):
            sum(None, 4)

def sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError(' els arguments han de ser int o float')
    return a + b

#sum ('a',3
#unittest.main()

from datetime import datetime, date

dict = {'name': 'Damia',
        'age': 17,
        'birth_date': datetime.strptime('24-05-07',"%d-%m-%y").date(),
        "programming_languages": ['python', 'PSInt']
}

class TestDate(unittest.TestCase):

    def test_field_exist(self):
        self.assertIn('name', dict)
        self.assertIn('name', dict)
        self.assertIn('name', dict)
        self.assertIn('name', dict)

    def test_data_is_correct(self):
        self.assertIsInstance(dict['name'],str)
        self.assertIsInstance(dict['age'],int)
        self.assertIsInstance(dict['birth_date'],date)
        self.assertIsInstance(dict['programming_languages'],list)

unittest.main()