import random

# Создание списка 10 рандомных чисел от 1 до 100
num = [random.randint(1, 100)
           for _ in range(10)]
print("Список чисел:", num)

# Нахождение макс и мин значения
print("Максимальное число:", max(num))
print("Минимальное число:", min(num))

# Вычисление суммы чисел 
print("Сумма чисел:", sum(num))

# Сортировка списка по возрастанию
sorted_num = sorted(num)  
print("Отсортированный список:", sorted_num)