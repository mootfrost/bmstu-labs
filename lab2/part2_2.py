"""
Автор: Семейкин Андрей Андреевич
Группа: ИУ7-14Б
Часть 2, задание 2, вариант 2: определение принадлежности замкнутой области
"""

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

# Ввод координат точки с клавиатуры
x = input('Введите х координату точки: ')
if is_number(x) and (x := float(x)) < 10e100:
    y = input('Введите y координату точки: ')
    if is_number(y) and (y := float(y)) < 10e100:
        # Проверка на принадлежность области
        if -6 <= x < 6 and \
                (y <= 0 and (y <= -0.25 * x ** 2 + 1) and ((y >= 2 * x + 4) or (y >= -2 * x + 4)) or
                 y > 0 and (y >= -0.25 * x ** 2 + 1) and (y <= 2 * x + 4) and (y <= -2 * x + 4)):
            print('Точка принадлежит замкнутой области')
        else:
            print('Точка не принадлежит замкнутой области')
    else:
        print('y не является числом или слишком большое')
else:
    print('x не является числом или слишком большое')


