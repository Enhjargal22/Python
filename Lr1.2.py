text = input("Введите текст: ").lower()
vowels_ru = "аеёиоуыэюя"
consonants_ru = "бвгджзйклмнпрстфхцчшщ"

vowel_count = 0
consonant_count = 0

vowel_letters = []

words = text.split()
for word in words:
    for letter in word:
        if letter in vowels_ru:
            vowel_count += 1
            vowel_letters.append(letter)
        elif letter in consonants_ru:
            consonant_count += 1

print("Количество гласных букв:", vowel_count)
print("Количество согласных букв:", consonant_count)

if vowel_count == consonant_count:
    print("Гласные буквы в тексте:", ' '.join(vowel_letters))

word_count = len(words)
print("Количество слов в тексте:", word_count)
