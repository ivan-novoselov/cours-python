#2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


my_list = input('Введите несколько цифр через пробел: ')
my_list = my_list.split()
print(my_list)
a = 0
print(len(my_list)//2)

for i in range(len(my_list)//2):
    my_list[a], my_list[a + 1] = my_list[a + 1], my_list[a]
    a = a+2
print(f'Решение: {my_list}')








# elem_list1 = input('Напишите имя:  ')
# elem_list2 = input('Сколько вам лет:  ')
# elem_list3 = input('Напишите название месяца:  ')
# elem_list4 = input('Напишите номер месяца:  ')
# elem_list5 = input('Напишите букву:  ')
#
# my_list = [elem_list1, elem_list2, elem_list3, elem_list4, elem_list5]
# print(f'Список: {my_list}')
