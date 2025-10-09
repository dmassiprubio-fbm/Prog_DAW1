'''
1️⃣ Crea dues variables de tipus data (datetime):
    - Una primera que representi la data (dia, mes, any, hora, minut, segons) actual.
    - Una segona que representi la teva data de naixement (pots inventar l'hora).
 2️⃣ Calcula quants d'anys han passat entre els dues.

DIFICULTAT EXTRA (Puntua si el resols totsol):
3️⃣ Utilitzant la data del teu aniversari, formatéjala i mostra el resultat de 10 formes diferents.

Per exemple:
    - Dia, mes i any.
    - Hora, minut i segons.
    - Dia de l'any.
    - Dia de la setmana.
    - Nom del mes.
    - ...
'''

from datetime import datetime
import locale

now = datetime.now()
print(now)

birth_day = datetime(2007,5,24,2,33,54)
print(birth_day)

diff = now - birth_day
print(type(diff))
print(f'Han passat {diff.days // 365} anys')

'''
extra
'''

print(birth_day.strftime('%d/%m/%Y'))
print(birth_day.strftime('%H:%M:%S'))
print(birth_day.strftime('%d/%m/%y'))
print(birth_day.strftime('%d/%B/%Y'))
print(birth_day.strftime('%d/%m/%Y-%I%p'))
print(birth_day.strftime('%d/%m/%Y-%H'))

#Locales time
print(birth_day.strftime('%c'))
print(birth_day.strftime('%X'))
print(birth_day.strftime('%x'))

locale.setlocale(locale.LC_ALL, '')
print(birth_day.strftime('%c'))
print(birth_day.strftime('%X'))
print(birth_day.strftime('%x'))