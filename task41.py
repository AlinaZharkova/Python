# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит 
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел.
# Ввод:
# 5               5
# 1 2 3 4 5       1 5 1 5 1
# Вывод:
# 0               2

n=int(input("input n: "))
set_n=[]
for i in range(n):
    x=int(input("input number from n: "))
    set_n.append(x)
print("set_n: ",set_n)

def neighbours_less(array):  # функция выводит кол-во пар, когда оба соседних элемента меньше исходного, в массиве
    count = 0
    for i in range(1, len(array)-1):
        if array[i] > array[i-1] and array[i] > array[i+1]:
            count += 1
    return count

print(neighbours_less(set_n))