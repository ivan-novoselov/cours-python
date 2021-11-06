#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input('Введите пожалуйста число от 1 до 9: ')
print()
number_2 = int(number+number)
number_3 = int(number+number+number)
number_sum = int(number)+number_2+number_3
print(f'{int(number)}+{number_2}+{number_3}={number_sum}')
print()
print(f'Результат = {number_sum}')

