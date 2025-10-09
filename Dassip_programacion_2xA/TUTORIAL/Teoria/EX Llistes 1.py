#1. Introduir 5 valors i ordenarlos de mayor a menor.
my_list =list()
contador = 0
while contador < 5:
    num=(int(input("Introdueix un valor: ")))
    my_list.append(num)
    contador = contador +1
my_list.sort()
my_list.reverse()
print(my_list)
