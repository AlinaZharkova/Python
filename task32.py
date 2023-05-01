# Определить индексы элементов массива (списка),значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

rand_list=[]
n=15
for i in range(n):
    rand_list.append(random.randint(-15, 15))
print(rand_list)

min_number = int(input("Введите МИНИМУМ для задания диапазона: "))
max_number = int(input("Введите МАКСИМУМ для задания диапазона:  "))

for i in range(n):
    if min_number <= rand_list[i] <= max_number:
        print(i)