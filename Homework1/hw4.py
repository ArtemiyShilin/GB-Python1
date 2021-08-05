# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

numbers = int(input('Введите число - '))
max = numbers % 10
while numbers >= 10:
    numbers = numbers // 10
    if max < numbers % 10:
        max = numbers % 10
print(max)