### bucles ###

# while

my_value = 100
while my_value >= 0:
    print(my_value)
    my_value = my_value - 5

my_value = 0
while my_value <= 100:
    print(my_value)
    my_value = my_value + 5
### ej ###
my_value1 = 0
while my_value1 <= 100:
    if my_value1 % 3 == 0:
        print("El", my_value1, "es míltiplo de 3.")
    my_value1 = my_value1 + 1


# For   (solo para las listas),  no tiene indice, le todo lo que hay en la lista

my_list = ["a", "b", "c"]
for letter in my_list: #Letter cojerá el valor de cada elemento de my_list
    print(letter)

#range sirve para contaodres numericos 
for i in range(10): #con un parametro el contador ira de 0 hasta n-1(n es el valo que le damos al contador)
    print(i)

for i in range(4, 10): #con dos parametros, el contador ira de "a" hasta "b-"1(a=4 i b=10)
    print(i)

for i in range(1, 10, 2): ##con tres parametros, el contador ira de "a" hasta "b-"1(a=4 i b=10) i el tercer parametro determina los saltos que tiene que hacer (c=2)
    print(i)

for i in range(10, 1, -1): #Sirve para ir en un contador hacia atrás(siempre los tres parametros)
    print(i)

##########################################################################################################################
assignatures=["Matemàtiques", "Física", "Química", "Biologia", "Programació"]
print(assignatures)
my_list_notes=[]
for assignatura in assignatures:
    notes=input("Que nota has tret a l'assignatura de " + assignatura + ": ")
    my_list_notes.append(notes)
    
for assignatura, nota in zip(assignatures, notes): # para usar el zip, las dos listas tienen que tener el mismo  numero de elementos
    print("A l'assignatura", assignatura, "he tret un", nota)

################################################

assignatures=["Matemàtiques", "Física", "Química", "Biologia", "Programació"]
assignatures.sort()
for assignatura in assignatures:
    print(assignatura)#no esta ordenado con las notas. Si queremos que las notas esten ordenadas con las assignaturas , hay que "assignatures.sort()" justo debajo de la lista principal.

########################################
    
assignatures=["Matemàtiques", "Física", "Química", "Biologia", "Programació"]
assignatures.sort()
my_list_notes=[]
for assignatura in assignatures:
    notes=input("Que nota has tret a l'assignatura de " + assignatura + ": ")
    my_list_notes.append(notes)
    
for assignatura, nota in zip(assignatures, notes): # para usar el zip, las dos listas tienen que tener el mismo  numero de elementos
    print("A l'assignatura", assignatura, "he tret un", nota)
