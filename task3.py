# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32

# import math
# class1=int(input('Введите кол-во учащихся в классе 1: '))
# class2=int(input('Введите кол-во учащихся в классе 2: '))
# class3=int(input('Введите кол-во учащихся в классе 3: '))

# print(f"минимальное количество парт, которое нужно приобрести = {math.ceil((class1+class2+class3)/2)}")

a = int(input())
b = int(input())
c = int(input())
a1 = (a + 1) // 2
b1 = (b + 1) // 2
c1 = (c + 1) // 2
s = a1 + b1 + c1
print(s)