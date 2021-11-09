#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка.
# Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].



my_list = [9, 6, 4, 4, 5, 3, 3, 4, 4]
print(my_list)

num = int(input('Введите цифру: '))
inserted = False
# el_index = 1
for elem in my_list:
    if num > elem:
        el_index = my_list.index(elem)+1
        my_list.insert(el_index, num)
        inserted = True
        break
if not inserted:
    my_list.append(num)
print(my_list)


# my_list = [9, 6, 4, 4, 5, 3, 3, 4, 4]
# print(my_list)
#
# num = int(input('Введите цифру: '))
# inserted = False
# for index, elem in enumerate(my_list):
#     if num > elem:
#         my_list.insert(index, num)
#         inserted = True
#         break
# if not inserted:
#     my_list.append(num)
# print(my_list)











