# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

a= int(input("Введите натуральное число a>1: "))
n=0
n1=1
i=2
t=0
count=0
while a>count:
    count=n+n1
    t=n1
    n1=n1+n
    n=t
    if a==count:
        break
    i+=1
if count!=a:
    print(-1)
else:
    print(i+1)        