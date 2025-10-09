#3. Introduce 10 numeros y invierte la lista
my_list =list()
contador = 0
while contador < 10:
    num=(int(input("Introdueix un valor: ")))
    my_list.append(num)
    contador = contador +1
my_list.reverse()#para cambiar el orden
print(my_list)