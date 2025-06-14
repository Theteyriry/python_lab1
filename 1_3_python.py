# Запрашиваем число n
n = int(input("Введите число n: "))

# Выводим числа от n до 1 в обратном порядке
print("Числа от n до 1:")
current = n
while current >= 1:
    print(current, end=" ")
    current -= 1
print()

# Выводим факториал числа n
n_fact = 1
current = 1
while current <= n:
    n_fact *= current
    current += 1
print("Факториал", n, ":", n_fact)