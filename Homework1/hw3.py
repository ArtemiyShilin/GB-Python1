# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

numbers = input('Ввежите число n: ')
# # sum = int(numbers)
# # sum1 = int(numbers + numbers)
# # sum2 = int(numbers + numbers + numbers)
# sum3 = sum + sum1 + sum2
sum = int(numbers) + int(numbers*2) + int(numbers*3)
print(sum)