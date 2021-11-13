#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_user_data(name, surname, birthdate, city, email, tel):
    result_user_data = (f'{name} {surname} {birthdate} {city} {email} {tel}')
    return result_user_data


name1 = input('Name: ')
surname1 = input('Surname: ')
birthdate1 = input('Birthdate: ')
city1 = input('City: ')
email1 = input('email: ')
tel1 = input('tel: ')

data_list = my_user_data(name = name1, surname = surname1, birthdate = birthdate1, city = city1, email = email1, tel = tel1)
print(data_list)




