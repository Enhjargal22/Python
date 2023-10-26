my_dict = {'a': 12, 'b': 13, 'c': 56, 'd': 400, 'e': 58, 'f': 20}

sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])

top_3 = sorted_dict[:3]

keys_with_smallest_values = [item[0] for item in top_3]

print("Три ключа с самыми маленькими значениями:", keys_with_smallest_values)
