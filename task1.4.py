#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

#number = input("Введите пожалуйста целое положительное число: ")
#number2 = list(number)
#print(number2)
#number3 = max(number2)
#print(f'Самая большая цифра: {number3}')

#Решение нашел, но не через while

number = int(input("Введите пожалуйста целое положительное число: "))
number1=0
while number > 0:
    if number1 < number % 10:
        number1 = number % 10
    number = number // 10

print(f'Самое большое число: {number1}')
