#Бондаренков Ум-252 Практика 5
#Задание 10

text='Convert the string so that each word starts with a capital letter.'
text=text.split()
for i in range(len(text)):
    text[i] = text[i].capitalize()
print(' '.join(text)) 