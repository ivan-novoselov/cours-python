#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input("Сколько времени вы спите, в секундах? "))
print(f"Я сплю {time} секунд")
hours = time//3600
minutes = (time%3600)//60
second = (time%3600)%60
print()
print(f'{hours:02}:{minutes:02}:{second:02}')
print()
print()
print(f"{hours} часов")
print(f'{minutes} минут')
print(f'{second} секунд')
