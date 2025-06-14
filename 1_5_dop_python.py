import random

# Генерация 20 рандомных чисел от 1 до 100 
num = [random.randint(1, 100) for _ in range(20)]

# Вывод чётных чисел
print("Чётные числа:")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")
print()

# Вывод кратных 3  
print("Числа, кратные 3:")
for n in num:
    if n % 3 == 0:
        print(n, end=" ")
print()

# Вывод среднего арифметического
average_num = sum(num) / len(num)
print("Среднее арифметическое:", average_num)