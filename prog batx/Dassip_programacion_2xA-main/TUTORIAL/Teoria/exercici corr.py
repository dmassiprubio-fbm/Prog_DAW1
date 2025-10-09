#################################
#EX 3
n1 = int(input("Introdueix un nombre:"))

if n1 % 15 == 0:
    print(n1, "és múltiple de tot dos")
elif n1 % 3 == 0:
    print(n1, "és múltiple de 3")
elif n1 % 5 == 0:
    print( n1, "és múltiple de 5")

#############################
#EX 5
n1 = int(input("Introdueix el costat d'un quadrat/cub:"))
op = input("Introdueix el que vols fer: Area , perímetre o volum:")

if op == "area":
    print("L'àrea del queadrat és: ", n1 ** 2)

elif op == "perímetre":
    print("El perímetre del quadrat és de: ", n1 * 4)

elif op == "volum":
    print("El volum del cub és de: ", n1 ** 3)

###################################
#EX 6
n1 = int(input("Introdueix l'altura de l'arbre:"))
estrellita = "*"
while n1 > 0:
    print(estrellita)
    n1= n1 - 1
    estrellita = estrellita + "*"
