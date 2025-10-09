### Conditional ###

my_condition = "Alba" < "Benito"
if my_condition:
    print("Alba és més petita que Benito")

print("continua normal ")

my_condition = 10 < 2
if my_condition:
    print("10 és més gran que 2")

print("continua normal")

my_condition =  4 < 2
if my_condition:
    print("el primer és més gran que el segon")
else:
    print("el segon és més gran que el primer")

#Com calcular si es par o inpar
my_number = int(input()) #Llegim per teclat i guardam el valor dins la variable my_number y convertim el valor a int.
if my_number % 2 == 0 : #mirma si my_number modul 2 es igual a 0.
    print("el number és par") # mostyram el missatge.
else: #Entrarà aquí si no es compleix lacondició anterior, és a dir, si el reidu es 1.
    print("El nombre es impar")# Mostram el miisatge contrari.

my_number = int(input()) 
if my_number % 2 == 0 : 
    print("el number és par") 
else: 
    print("El nombre es impar")

my_number = int(input()) 
if my_number % 3 == 0 : 
    print("el number és multiple de 3") 
else: 
    print("El nombre no és multiple de 3")

# Identificar si ets múltiple de2, 3, 5 o 7
my_number =int(input())
if my_number % 2== 0:
    print("El nombre és múltiple de 2")
elif my_number % 3 == 0:
    print("El nombre és múltiple de 3")
elif my_number % 5 == 0:
    print("El nombre és múltiple de 5")
elif my_number % 7 == 0:
    print("El nombre és múltiple de 7")
else:
    print("no és múltiple ni de 2 , 3, 5 ni 7")
