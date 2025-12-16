#Бондаренков Ум-252 Практика 5
#Задание 14

text = "аллея арка море семья земля окно акула"

words = text.split()
result = []

for word in words:
    if word[0] == 'а' or word[-1] == 'я':
        result.append(word)

print(' '.join(result))