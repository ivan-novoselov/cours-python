#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
#и возвращает сумму наибольших двух аргументов.

def my_sum(a,b,c):
    sum_abc = a + b + c
    sum_2_max = sum_abc - min(a,b,c)
    return sum_2_max
a1 = int(input('a: '))
b1 = int(input('b: '))
c1 = int(input('c: '))
result_my_sum = my_sum(a1,b1,c1)
print(result_my_sum)


