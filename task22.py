# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). #
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите число элементов первого списка: "))
num_list1=[]
for i in range(n):
    num = int(input("Введите элемент списка 1: "))
    num_list1.append(num)
print(f'список 1: {num_list1}')

m = int(input("Введите число элементов второго списка: "))
num_list2 = []
for i in range(m):
    num = int(input("Введите элемент списка 2: "))
    num_list2.append(num)
print(f'список 2: {num_list2}')

for i in range(n):
    for j in range(n-i-1):
        if num_list1[j] > num_list2[n-i-1]:
            num_list1[j], num_list2[n-i-1] = num_list2[n-i-1], num_list1[j]
            
num_list3 = set(num_list1 + num_list2)

print(f'общий список: {num_list3}')        