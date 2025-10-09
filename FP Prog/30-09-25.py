# nums = [1,2,3,4,5,6,7,8,9,10]
# for i in nums:
#     print(i)

# for i in range(1, 11):
#     print(i)

# for i in range(1, 10+1):
#     print(f'{2} * {i} = {2*i} ')

'----------------------------------------------------------------------'

# a = int(input('1r numero: '))
# b = int(input('2n numero: '))

# sumario = 0

# if b >= a:
#     for i in range(a, b+1):
#         sumario = sumario + i
#         print(sumario)
# else: 
#     print('el primer numero tiene que ser menor que ele segundo')

'----------------------------------------------------------------------'
#EJERCICIOS CLASSROOM
'----------------------------------------------------------------------'

# print('primera llista')
# for i in range(1,11):
#     print(i)
# print('segunda lista')
# for i in range(1, 11):
#     print(2*i)
# print('tercera lista')
# for i in range(10):
#     print(20+(2*i))
# print('cuarta lista')
# for i in range(11):
#     if i%2 == 0:
#         print(10+(2*i))
# print('quinta lista')
# for i in range(9):
#     print(40-(i*5))

'----------------------------------------------------------------------'

# num1=()
# num2=()

# while num1 >= num2:
#     print('el primero tiene que ser menor al segundo')
#     num1 = int(input('introdiuce un numero: '))
#     num2 = int(input(f'introduce un numero mayor que {num1}: '))
#     for i in range(num1, num2):
#         if i % 2 == 0:
#             print(f'{i} es par')
#         else:
#             print(f'{i} es impar')

'----------------------------------------------------------------------'

num1=()
num2=()

sumario = 0

while num1 >= num2:
    print('el primero tiene que ser menor al segundo')
    num1 = int(input('introdiuce un numero: '))
    num2 = int(input(f'introduce un numero mayor que {num1}: '))
    for i in range(num1, num2 + 1):
        sumario = sumario + i
    print(sumario)        

'----------------------------------------------------------------------'

num = int(input('introduce un numero: '))
res = 1

for i in range(1, num+1):
    res = res * i
print(res)

'----------------------------------------------------------------------'

