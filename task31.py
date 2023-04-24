# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию
#считаем, что ряд Фибоначчи начинается так: 1 2 3 5 8 13 21 34

n = int(input("Введите число: "))

def fibonachi(n):
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        return fibonachi(n-1) + fibonachi(n-2)
    
print(fibonachi(n))
