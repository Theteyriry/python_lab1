# Вводим число n
n = int(input("Введите число n: "))

# Выводим все числа от 1 до n
print("Все числа от 1 до n:")
for i in range(1, n + 1):
    print(i, end=' ')
print() 

# Выводим квадраты всех чисел от 1 до n
print("Квадраты чисел от 1 до n:")
for i in range(1, n + 1):
    print(i**2, end=' ')
print()  

# Выводим сумму всех чисел от 1 до n
sum_numbers = sum(range(1, n + 1))  
print("Сумма всех чисел от 1 до n:", sum_numbers)  