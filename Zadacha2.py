#  Задайте натуральное число N. Напишите программу, которая составит 
#  список простых множителей числа N.

# *Пример*   - при N=236     ->        [2, 2, 59]

n = int(input('Введите число\n'))

result = []
i = 2


while n % i == 0:
    result.append(i)
    n /= i
else:
    result.append(n)
print(result)