
cont = int(input())
num2 =  1

while num2 <= cont:
    numero = int(input())
    binari = []

    while numero != 1 and numero != 0:
        resto = numero % 2 
        resto = str(resto)
        numero = numero // 2
        binari.insert(0,resto)
    numero = str(numero)
    binari.insert(0,numero)
    binari2 =''.join(binari)
    print(binari2)
    num2 = num2 + 1