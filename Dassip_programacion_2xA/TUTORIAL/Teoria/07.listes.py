### LISTS ###

my_list = [] #llista buida
my_other_list =[1,2,3,4] #llista amb 4 nombres
my_string_list = ["Dani", "Alba", "Xisco", "Mati", "Carla"]
my_other_other_list = ["Guillem", "Mas", 36, True]

print(len(my_list))
print(len(my_other_list))
print(len(my_string_list))

my_sum_list = my_string_list + my_other_list
print(len(my_sum_list))#Saber cuantos elelemntos hay
print(my_sum_list)

my_mult_num = my_string_list * 3
print(my_mult_num)

# Accessos
# list= ["A","B","C","D","E","F"] --> 6
# list= (posicion) ["A"(0),"B"(1),"C"(2),"D"(3),"E"(4),"F"(5)] --> 6
# list= (posicion) ["A"(-6),"B"(-5),"C"(-4),"D"(-3),"E"(-2),"F"(-1)] --> 6 print(len(list-1))
print(my_string_list[0])
print(my_string_list[4])
print(my_string_list[-1])

my_string_list[1]="Damià"
print(my_string_list)

### Funciones de les llistess¡###
my_new_list = [3,4,1,3,4,5,6,7,6,4,3,4,5]
print(my_new_list.count(4)) # Per contar quants d'elements d'aquests tipus hi ha
print(my_string_list.index("Dani")) # Per veure quina posició ocupa el valor

my_string_list.append("Alba")
print(my_string_list)

my_string_list.remove("Dani")
print(my_string_list)

my_string_list.reverse()
print(my_string_list)

my_string_list.sort()
print(my_string_list)

my_new_list.sort()
print(my_new_list)


alumns= ["Dani", "Alba", "Xisco", "David"]

alumns.sort()
print(alumns.count("alba"))
