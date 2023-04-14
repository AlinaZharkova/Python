# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

list=[1, 1, 2, 0, -1, 3, 4, 4] #данный список
n=len(list) #считаем сколько элементов в списке
print(list)
for i in range(n):
    for j in range(n-i-1):
        if list[j]>list[n-1-i]:
            list[j],list[n-1-i]=list[n-1-i],list[j]
print("упорядоченный список:", list)
k=1 #счетчик уникальных значений
for i in range(n-1):
    if list[i]!=list[i+1]:
        k+=1
print("кол-во уникальных элементов: ",k)

# второй вариант решения задачи
# n=[1, 1, 2, 0, -1, 3, 4, 4]
# itog = []
# for i in n:
# if i not in itog:
# itog.append(i)
# print (len(itog))