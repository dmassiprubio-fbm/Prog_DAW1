'''
1️⃣Crea exemples utilitzant tots els tipus d'operadors de Python:

    Aritmètics, lògics, de comparació, assignació, identitat, pertinença, bits...

2️⃣Utilitzant les operacions amb operadors que tu vulguis, crea exemples que representin tots els tipus d'estructures de control que existeixen a Python:

    Condicionals, iteratives, excepcions...

3️⃣Has de fer print per consola del resultat de tots els exemples.

DIFICULTAT EXTRA (Puntua si el resols totsol):
4️⃣Crea un programa que imprimeixi per consola tots els números compresos entre 10 i 55 (inclosos), parells, i que no són ni el 16 ni múltiples de 3.
'''

###Aritmetics###

print(f'Suma: 10 + 3 = {10+3}')
print(f'Resta: 10 - 3 = {10-3}')
print(f'Multiplicacio: 10 * 3 = {10*3}')
print(f'Diviso: 10 / 3 = {10/3}')
print(f'Exponencial: 10 ** 3 = {10**3}')
print(f'Modulo: 10 % 3 = {10%3}')
print(f'Div Entera: 10 // 3 = {10//3}')

###Comparadors### (Verdero o Falso)

print(f'Igaldad: 10 == 3 = {10==3}')
print(f'Desigualdad: 10 != 3 = {10!=3}')
print(f'Major: 10 > 3 = {10>3}')
print(f'Menor: 10 < 3 = {10<3}')
print(f'Major o igual: 10 >= 3 = {10>3}')
print(f'Menor o igual: 10 <= 3 = {10<3}')

###Logics###

print(f'AND: 10 + 3 == 13 and 5-1 == 4 { 10 + 3 == 13 and 5-1 == 4 }') #TODAS VERTDERES PER TR1UE
print(f'OR: 10 + 3 == 13 or 5-1 == 1 { 10 + 3 == 13 or 5-1 == 1}') #UNA VERTADERA PER TRUE
print(f'NOT: not 10 + 3 == 13 {not 10 + 3 == 13}') #NEGAM EL QUE POSA, SERVEIX PER CAMBIAR EL QUE TOCA, DE TRUE A FALSE I DE FALSE A TRUE

###Asignació###

my_num = 11
print(my_num)
my_num += 1
print(my_num)
my_num -= 1
print(my_num)
my_num *= 1
print(my_num)
my_num /= 1
print(my_num)
my_num //= 1
print(my_num)
my_num %= 1
print(my_num)

###Identitat###

my_new_num = my_num
print(f'my num is my_new_num és {my_num is my_new_num}')
print(f'my num is not my_new_num és {my_num is not my_new_num}')

###Pertinença###

print(f"'u' in 'Guillem' {'u' in 'Guillem'}")
print(f"'Gui' in 'Guillem' {'Gui' in 'Guillem'}")
print(f"'u' not in 'Guillem' {'u' not in 'Guillem'}")

###Bits###

a = 10 # 1010
b = 3 # 0011

print(f'AND: 10 & 3 {10 & 3}') # 0010 -> 2
print(f'OR: 10 | 3 {10 | 3}') # 1011 -> 11
print(f'XOR: 10 ^ 3 {10 ^ 3}') # 1001 -> 9
print(f'NOT: ~10 {~10}')  # CONVIERTNE 1 EN 0 Y 0 EN 1

'''
ESTRUCTURES DE CONTROLS
'''

#Condicional 

my_string = 'Guillem'
if my_string == 'Guillem':
    print("my_string es 'Guillem'" )
elif my_string == 'GMA':
    print("my_string es 'GMA'")
else:
    print("no es ni una ni l'altra")

###Iteratives###

i = 0
while i < 10:
    print(i)
    i += 1

for i in range(10):
    print(i)

### Control d'excepcions###

try:
    print(10/0)
except:
    print("S'ha produït un error. No se puede dividir entre 0 payaso")
finally:
    print("S'ha acabat el control de error")

###Crea un programa que imprimeixi per consola tots els números compresos entre 10 i 55 (inclosos), parells, i que no són ni el 16 ni múltiples de 3###


for i in range(10,56,2):
     if i != 16 and not i % 3 == 0:
         print (i)     
        

