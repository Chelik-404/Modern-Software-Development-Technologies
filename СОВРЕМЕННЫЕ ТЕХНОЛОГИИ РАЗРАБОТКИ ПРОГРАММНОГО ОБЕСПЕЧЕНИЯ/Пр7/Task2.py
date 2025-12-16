#Бондаренков Ум-252 Практика 7
#Задание 2
#Вариант 3

def sort_word(word):
    letters = list(word)
    letters.sort()
    return ''.join(letters)

text = input("Введите строку: ")

words = text.split()
result = []

for word in words:
    result.append(sort_word(word))

print(' '.join(result))