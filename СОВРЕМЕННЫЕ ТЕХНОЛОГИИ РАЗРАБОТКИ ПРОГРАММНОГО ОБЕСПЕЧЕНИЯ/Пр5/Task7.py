#Бондаренков Ум-252 Практика 5
#Задание 7

text=input('Введите текст: ')
newText=''
for i in range(len(text)):
    if i<len(text)//2 and text[i]=='п':
        newText+='*'
    else:
        newText+=text[i]
print('Результат :',newText) 