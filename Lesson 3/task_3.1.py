
#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_div(num1, num2):
    if num2 == 0:
        return 'You can not divide to 0'
    else:
        return num1/num2

v = int(input('num_1:  ')),int(input('num_2:  '))
num1 = int(input('num_1:  '))
num2 = int(input('num_2:  '))
print(my_div(num1, num2))





















# def my_div(num1, num2):
#     result_my_div = num1 / num2
#     return result_my_div
#
# num1 = int(input('введите число:  '))
# num2 = int(input('введите число:  '))
# if num2 == 0:
#     print('число не равно "0"!!!')
#     print()
#     num2 = int(input('введите другое число:  '))
#
# div_num = num1/num2
# print(f'Результат деления: {div_num}')
