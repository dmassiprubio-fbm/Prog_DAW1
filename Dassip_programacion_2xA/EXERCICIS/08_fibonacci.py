def fibonnacci(number):
    if number == 1:
        return 1
    if number == 2:
        return 1
    else:
        return fibonnacci(number-1) + fibonnacci(number-2)
num = int(input())
print(fibonnacci(num))