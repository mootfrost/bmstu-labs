"""
Автор: Семейкин Андрей Андреевич
Группа: ИУ7-14Б
Часть 2, задание 1, вариант 1: определение значения функции
"""
from math import sqrt
def is_number(s: str):
    if not s:
        return False

    if s[0] in ['-', '+']:
        s = s[1:]
        if not s:
            return False

    dot = False
    exp = False
    dig = False
    exp_digit = False
    i = 0
    while i < len(s):
        if s[i].isdigit():
            if exp:
                exp_digit = True
            else:
                dig = True
        elif s[i] == '.':
            if dot or exp:
                return False
            dot = True
        elif s[i] == 'e':
            if exp or not dig:
                return False
            exp = True
            if i + 1 < len(s) and s[i + 1] in ['-', '+']:
                i += 1
            if i + 1 >= len(s):
                return False
            exp_digit = False
        else:
            return False
        i += 1
    if exp:
        return dig and exp_digit
    else:
        return dig

x = input('Введите значение аргумента функции х: ')
if is_number(x) and (x := float(x)) < 1e100:
    if x <= -6:  # функция 4
        y = -(x - 4) / 2 - 10
    elif -6 < x < 4:  # функция 1
        y = -(x / 2) ** 2 + 4
    elif 4 <= x < 8:  # функция 2
        y = sqrt(x - 4)
    else:  # функция 3
        y = (x - 4) / 2
    print(f'Значение функции f({x:g}) = {y:.5g}')
else:
    print('Число некорректно')