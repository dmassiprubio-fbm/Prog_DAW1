#2. Introduce una lista de nombres fins posar un 0 y ordenala a alfabeticamente.
my_list_1=[]
nombre= ""
nombre= input(("Introdueix el nombre:"))
while nombre != "0":
    nombre= input(("Introdueix el nombre:"))
    if nombre != "0":#evitamos meter el 0 en la lista
        my_list_1.append(nombre)
my_list_1.sort()
print(my_list_1)