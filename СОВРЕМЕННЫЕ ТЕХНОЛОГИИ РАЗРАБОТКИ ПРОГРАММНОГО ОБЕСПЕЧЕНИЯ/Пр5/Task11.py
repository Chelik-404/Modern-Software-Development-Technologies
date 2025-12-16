#Бондаренков Ум-252 Практика 5
#Задание 11

text = "нн привет! нннн! как дела!! ннннннн!"

text = text.replace('!', '.')

max_n = 0
current_n = 0

for char in text:
    if char == 'н':
        current_n += 1
        if current_n > max_n:
            max_n = current_n
    else:
        current_n = 0

print("Преобразованный текст:", text)
print("Максимальная длина последовательности 'н':", max_n)