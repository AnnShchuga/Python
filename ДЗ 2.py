# Задание 1

float_num = input('введите вещественное число: ')
print(type(float_num))
sum = 0
for i in float_num:
    if i != '.':
        sum += int(i)
print(sum)


# Задание 2

n = int(input('input N: '))
factorial = 1
for i in range(1, n+1):
    factorial *= i
    print(factorial, end=' ')

# Задание 3

n = int(input('Введите число: '))

def get_squerence(n):
    return [round((1 + 1 / x)**x, 3) for x in range (1, n + 1)]

nums = get_squerence(n)
print(nums)
print(round(sum(nums), 3))


# Задание 4

for i in range(10):
    numbers.append(randint (-10,10))
print(numbers)

def get_numbers(numbers):
    count =0
    for element in numbers:
        count +=1
    return count
print('Количество элементов: ', get_numbers(numbers))

a = int(input('Введите a: '))
b = int(input('Введите b: '))

for i in range(len(numbers)):
    mult = numbers[a -1]*numbers[b - 1]
print(f'Произведение элементов: {numbers[a -1]} * {numbers[b -1]} =', mult)

# Задание 5

import random
lst = [random.randint(0,10) for i in range(random.randint(5,20))]
print(f"исходный список:\n {lst}")
random.shuffle(lst)
print(f"список после перемешивания:\n{lst}")

# Задание 6

a = int(input('Введите a: '))
b = int(input('Введите b: '))

cnt = 0
pos = 0
while True:
    idx = a[pos:].find(b)
    if idx != -1:
        cnt += 1
        pos += idx + 1
    else:
        break
print(cnt)