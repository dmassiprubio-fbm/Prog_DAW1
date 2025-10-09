
'''
Crea un programa que s’encarregui de comprovar si un nombre és o no primer.
'''


cont = int(input())
num2 =  1
while num2 <= cont:
    
    num= int(input())
    result = 0
    for i in range(2,num):
    
        if num % i == 0:
            result = 1
            break
        else:
            result = 0


    if result == 1:
        print(False)
    elif result == 0:
        print(True)
    num2 = num2 + 1
        


