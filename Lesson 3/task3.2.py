#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_user_data(name, surname, birthdate, city, email, tel):
    result_user_data = [name + surname + birthdate + city + email + tel]
    return result_user_data

name = input('Name: ')
surname = input('Surname: ')
birthdate = input('Birthdate: ')
city = input('City: ')
email = input('email: ')
if '@' in email:
    tel = input('tel: ')
else:
    while '@' not in email:
        print('email введен неверно')
        email = input('email: ')
tel = input('tel: ')
while type(tel) is int:
    print('tel введен неверно')
    tel = input('tel: ')

data_list =(f'name-{name}; surname-{surname}; birthdate - {birthdate}; city - {city}; email - {email}; tel - {tel}')
print(data_list)




