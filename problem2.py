# Задача 2: Найдите сумму цифр трехзначного числа.

num = input('Введите трёхзначное число: ' )
sum  = 0
if len(num) <= 3:
    for i in num:
        sum = sum + int(i)
    print(f'Сумма чисел = {sum}') 
else:
    for i in num:
        sum = sum + int(i)
    print(f'Вы ввели не трёхзначное число, но так уж и быть... {sum} - сумма чисел.')