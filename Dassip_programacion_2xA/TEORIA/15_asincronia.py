'''
1️⃣ Crea un programa capaç d'executar de manera asíncrona una funció que simularà la petició del temps en determinades ciutats.

2️⃣ La funció imprimeix el nom, quan comença, el temps que durarà l'execució i quan finalitza.

3️⃣ Utilitzant el concepte d'asincronia i la funció anterior, crea la següent seqüència de funcions:
    - Una funció C que dura 3 segons.
    - Una funció B que dura 2 segons.
    - Una funció A que dura 1 segons.
    - Una funció D que dura 1 segons.
    - Les funcions C, B i A s'executen en paral·lel.
    - La funció D comença la seva execució quan les 3 anteriors han acabat.
'''

import random
import time
import datetime
import asyncio

async def get_time_weather(city):
    print(f'Inici sol·licitud per {city}... - Inici: {datetime.datetime.now()}')
    temp = random.randint(-5, 20)
    await asyncio.sleep(random.randint(1, 5))
    info =  {'city' : city, 'temp' : temp}
    print(f'Dades per {city} rebudes - Fi: {datetime.datetime.now()}')
    return info

async def main():
    
    cities = ['palma', 'llucmajor', 'barcelona', 'berlín', 'arenal']

    tasks = [get_time_weather(city) for city in cities ]

    info = await asyncio.gather(*tasks)
   
    for i in info:
        print(i)

asyncio.run(main())
