my_list = [12, 511, 'Python', 311, 122, 'love']

def is_even(num):
    if isinstance(num, int):
        return num % 2 == 0
    return False

def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

for i in range(len(my_list)):
    if is_even(my_list[i]):
        my_list[i] = sum_of_digits(my_list[i])

print(my_list)
