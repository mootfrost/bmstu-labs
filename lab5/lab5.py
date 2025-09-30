"""
Выполнил: Семейкин Андрей Андреевич
Группа: ИУ7-14Б
Лабораторная 5.
1) Построить таблицу аргументов и значений функции с заданным шагом
2) Построить график функции
"""


def func(b: float) -> float:
    """Вычисление значения функции из условия"""
    return (b**9) + (34 * b**8) - (2 * b**7) + (24 * b**6) - (76 * b**5) + (33 * b**4) - (b**3) + (3 * b**2) + (7 * b) - 33


start = -0.8  # начало
h = 0.05  # шаг
end = 1.2  # конец

# Вывод шапки таблицы
header = f'| {'X':^10} | {'Y':^10} |'
print('-' * len(header))
print(header)
print(f'|{'-' * (len(header) - 2)}|')

min_y = 1e1000
min_y_x = 0
max_y = -1e1000
steps = int((end - start) // h)
for i in range(steps + 2):
    x = start + h * i
    y = func(x)
    if y < min_y:
        min_y = y
        min_y_x = x
    max_y = max(max_y, y)
    print(f'| {x:<10.5g} | {y:<10.5g} |')
    x += h

print('-' * len(header))



legend_width = 7  # ширина легенды
graph_width = 150  # ширина отрисовки графика

points_cnt = -1
while not 4 <= points_cnt <= 8:
    points_cnt = int(input('Введите количество точек которые будут отмечены на оси Oy. От 4 до 8: '))

# Размещение чисел равномерно на прямой
point_gap = graph_width // (points_cnt - 1)
line = '{:.5g}'.format(min_y)
prev_offset = len(line)
for i in range(1, points_cnt):
    point = min_y + (max_y - min_y) / points_cnt * i
    fmt_point = '{:.5g}'.format(point)
    offset = len(fmt_point) // 2
    line += fmt_point.rjust(point_gap + offset - prev_offset)
    prev_offset = offset
print(' ' * legend_width + line)

# Отрисовка графика
for i in range(steps + 2):
    x = start + h * i
    y = func(x)
    point = int((y - min_y) / (max_y - min_y) * graph_width)
    print(f'{x:>.{legend_width - 2}g}'.rjust(legend_width - 1) + '|', end='')  # Вывод легенды

    graph_st = ' ' * (point - 1) + '*' + ' ' * (graph_width - point)  # Базовая строка графика
    # Добавление нуля, если он есть
    if min_y <= 0 <= max_y:
        z_point = int((0 - min_y) / (max_y - min_y) * graph_width)
        graph_st = graph_st[:z_point] + '|' + graph_st[z_point + 1:]
    print(graph_st)

print(f'Минимальное значение функции y_min = {min_y:.5g} достигается при значении аргумента b_min = {min_y_x:.5g}')


