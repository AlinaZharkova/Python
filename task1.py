# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700 m = 750 Output: 2

# import math
# n = int(input('Введите количество километров, которое проезжает машина за 1 день: '))
# m = int(input('Введите длину маршрута в километрах: '))


# print(f"чтобы проехать маршрут длиной {m} километров нужно {math.ceil(m/n)} дней")

n = int(input('Введите количество километров, которое проезжает машина за 1 день: '))
m = int(input('Введите длину маршрута в километрах: '))

print((m+n-1)//n)