# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input("Введите трехзначное число: "))

hundreds = (n % 1000) // 100
tens = (n % 100) // 10
units = (n % 10)

print(f"Полученные числа: {hundreds, tens, units}")
print(f"Cумма цифр трехзначного числа = {hundreds + tens + units}")
