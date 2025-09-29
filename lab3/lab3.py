"""
Автор: Семейкин Андрей Андреевич
Группа: ИУ7-14Б
Лабораторная 3
"""
from math import sqrt

ax, ay = map(int, input('Введите координаты точки A через пробел:').split())
bx, by = map(int, input('Введите координаты точки B через пробел:').split())
cx, cy = map(int, input('Введите координаты точки C через пробел:').split())

# Вычисление длин сторон
ab = sqrt((ax - bx) ** 2 + (ay - by) ** 2)
bc = sqrt((cx - bx) ** 2 + (cy - by) ** 2)
ca = sqrt((ax - cx) ** 2 + (ay - cy) ** 2)


if (ab < bc + ca) and (bc < ca + ab) and (ca < ab + bc):
    print(f'Длинна AB = {ab}')
    print(f'Длинна BC = {bc}')
    print(f'Длинна AC = {ca}')

    p = (ab + bc + ca) / 2  # полупериметр
    s = sqrt(p * (p - ab) * (p - bc) * (p - ca))  # площадь
    h = s * 2 / min(ab, bc, ca)  # максимальная высота
    print(f'Высота проведенная из наименьшего угла = {h:.5g}')

    # проверка равнобедренности
    if ab == bc or ab == ca or bc == ca:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник не равнобедренный')
    zx, zy = map(float, input('Введите координаты точки Z через пробел:').split())

    # Перемещение A в (0, 0)
    bx -= ax
    cx -= ax
    zx -= ax
    ax -= ax

    by -= ay
    cy -= ay
    zy -= ay
    ay -= ay

    # коэффициенты a*AB + b*AC = AP
    a = (zx * by - bx * zy) / (cx * by - bx * cy)
    l = (cx * zy - cy * zx) / (cx * by - bx * cy)
    if 0 <= a <= 1 and l >= 0 and a + l <= 1:
        print('Точка Z лежит внутри треугольника')
        # площадь параллелограмма / длина стороны = высота
        cross1 = abs(bx * zy - zx * by)
        dist1 = cross1 / sqrt(bx**2 + by**2)

        cross2 = abs(cx * zy - zx * cy)
        dist2 = cross1 / sqrt(cx**2 + cy**2)

        cross3 = abs((bx - cx)*(zy - cy) - (by - cy)*(zx - cx))
        dist3 = cross3 / sqrt((bx - cx)**2 + (by - cy)**2)

        max_dist = max(dist1, dist2, dist3)
        print(f'Самое большое расстояние от точки до стороны треугольника = {max_dist:.5g}')
    else:
        print('Точка Z не лежит внутри треугольника')
else:
    print('Такого треугольника не существует')