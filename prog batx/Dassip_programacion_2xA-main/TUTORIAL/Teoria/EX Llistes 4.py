#Introduceun lista de x  numeros y que ordene primero pares entre ellos y luego imparesentre ellos.
my_list_par=[]
my_list_impar=[]
num=0
while num!= -1:
    num= int(input("Introdueix un número:"))
    if num != -1:
        if num %2 == 0:
            my_list_par.append(num)
        else:
            my_list_impar.append(num)
my_list_par.sort()
my_list_impar.sort()
print(my_list_par + my_list_impar )