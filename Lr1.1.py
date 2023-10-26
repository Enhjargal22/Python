num = int(input("Введите натуральное число: "))

even_sum = 0

while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even_sum += digit
    num //= 10

print("Сумма чётных цифр в числе:", even_sum)
