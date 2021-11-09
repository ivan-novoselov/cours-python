#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.



num_month_list = int(input('Номер месяца: '))

#Решение через - dict:
my_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}
print(my_dict[num_month_list])

#Решение через - List:
season_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(season_list[num_month_list-1])









# my_str1 = 'hello world'
# my_str2 = 'It is me'
# my_str_3 = "H"+my_str1[1:]
# print(my_str_3)
# my_str_3 = my_str_3.split()
# print(my_str_3)
# print(my_str1.count('o' ))
# print(my_str1.index('w'))
# print(my_str1.isupper())
# my_list = list(my_str1)
# print(my_list)
# my_list[0]='R'
# my_list.insert(0,'!')
# print(my_list)

# for el in my_str1[::-1]:
#     print(el)
#
# print(my_str1[::-1])



#if(score_theory + score_practical > 100):
