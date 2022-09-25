# Задание 1

my_list = [2, 3, 5, 9, 3]
print(sum(my_list[1::2]))


# Задание 2

my_list = [2, 3, 4, 5, 6]
result_list = []
for i in range((len(my_list)+1)//2):
    result_list.append(my_list[i]*my_list[len(my_list)-1-i])
print(result_list)

# Задание 3


my_list = [1.1, 1.2, 3.1, 5, 10.01]
min = 1
max = 0
for i in my_list:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)
print(max-min)


# Задание 4

s = ""
n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while n != 0:
    s = str(n%2) + s
    n //=2
print(s)


# Задание 5

def Fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
userNumber = int(input('Enter any number: '))
for e in range(1, userNumber + 1):
    list.append(Fibonacci(e))
    list.insert(0, NegaFibonacci(e))
print(list)