### Funciones ###

def  operar_amb_nombres(num_a_operar1, num_a_operar2):
    suma = num_a_operar1 + num_a_operar2
    suma = suma * 20
    suma = suma +3
    return suma


num1 = int(input("Introdueix el nombre 1: "))
num2 = int(input("Introdueix el nombre 2: "))
contador =0
while contador < 20:
    suma = operar_amb_nombres(num1, num2)
    print(suma)
    contador = contador +1

num1 = int(input("Introdueix un altre nombre: "))
contador =0
while contador < 20:
    suma = operar_amb_nombres(num1, num2)
    print(suma)
    contador = contador +1
#######################################################################################################################
#Funció que retorni a la suma de dos valors

def operacio_nombres(valor1, valor2):
    suma = valor1 + valor2
    return suma
num1 = int(input("introdueix un nombre: "))
num2 = int(input("introdueix un nombre: "))
suma = operacio_nombres(num1, num2)
print(suma)

#########################################################################################################################

def suma_tres_valors(valor1, valor2, valor3):
    suma = valor1 +valor2 + valor3
    return suma
num1 = int(input("introdueix un nombre: "))
num2 = int(input("introdueix un nombre: "))
suma = suma_tres_valors(num1, num2, 10)
print(suma)

###########################################################################################################################
# par o impar
def impar_o_par(valor1):
    if valor1 % 2 == 0:
        print("És par") 
    else:
        print("És impar")
        
impar_o_par(5)
impar_o_par(4)
impar_o_par(6)
impar_o_par(1)

##############################################################################################################################
def positiu_negatiu(valor1):
    if valor1 >= 0:
        return "És postitu"
    else: 
        return "És negatiu"
    
print(positiu_negatiu(6))
print(positiu_negatiu(-9))

###############################################################################################################################
def mes_gran(valor1, valor2):
    if valor1 > valor2:
        return valor1
    else: 
        return valor2
    
print("El valor més gran és:", mes_gran(5, 6))
