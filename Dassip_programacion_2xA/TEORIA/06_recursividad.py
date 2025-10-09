''''
1️⃣Entén el concepte de recursivitat creant una funció recursiva que imprimeixi els números del 100 al 0.

DIFICULTAT EXTRA (Puntua si el resols totsol):

2️⃣Utilitza el concepte de recursivitat per a:

    Calcular el factorial d'un número concret (la funció rep aquest número).
    Calcular el valor d'un element concret (segons la seva posició) en la successió de Fibonacci (la funció rep la posició).
'''

def countdown(number):
    if number >= 0:
        print(number)
        countdown(number - 1)
    '''
    for i in range(100,-1,-1):
        print(i)
    '''
countdown(100)


def factorial(num):
    if num == 1:
        return 1
    else: 
        return num * factorial(num - 1)
    
print(factorial(5))

#Factorial 5 = 5*4*3*2*1

#successió de fibonnacci: 1,1,2,3,5,8,13,21

def fibonnacci(number):
    if number == 1:
        return 1
    if number == 2:
        return 1
    else:
        return fibonnacci(number-1) + fibonnacci(number-2)

print(fibonnacci())