# Функция 1
# def mul_elem_list(list_1):
#     result = 1
#     for elem in list_1:
#         # result = result * elem
#         result *= elem
#
#     result *= elem
#     return result
#
# abgf_list = [5, 5, 63]
# abgf_list.insert(0,158)
# print(abgf_list)
# mul_nums = mul_elem_list(abgf_list)
# print(mul_nums)


# Функция 2
# def mult_sum_list(list_1, list_2, num=3):
#     result = 0
#     for elem in list_1:
#         # result = result * elem
#         result += elem
#     for elem in list_2:
#         # result = result * elem
#         result += elem
#     result *= num
#     return result
#
# my_list_1 = [1, 2, 3, 4, 6, 7, 5, 10]
# my_list_2 = [5, 6, 4, 8, 5]
# # num_1 = 2
# # mul_nums = mult_sum_list(my_list_2, my_list_2, num_1)
# mul_nums = mult_sum_list(list_1=my_list_1, list_2=my_list_2, num=5)
# print(mul_nums)


#  Функция 3
# def add_elem_to_list(elem, list):
#     list.append(elem)
#
# my_list = [1, 2, 3, 4, 5, 6, 7]
# add_elem_to_list(8, my_list)
# print(my_list)

# функция 4
# def add_elem_to_list(elem, list=[]):
#     list.append(elem)
#     return list
#
# my_list = [1, 2, 3, 4, 5, 6, 7]
# print(add_elem_to_list(8))
# print(add_elem_to_list(9)) #будет ошибка, выведется вместо [9] выведется [8] и [9]


# # функция 5 (исправление ошибки из предыдущей функции)
def add_elem_to_list(elem, list=None):
    if list is None:
        #if not list (это тоже самое что и - if list is None)
        list = []
    list.append(elem)
    return list

# my_list = [1, 2, 3, 4, 5, 6, 7]
print(add_elem_to_list(8))
print(add_elem_to_list(9))