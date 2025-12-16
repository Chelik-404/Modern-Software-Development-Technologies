#Бондаренков Ум-252 Практика 5
#Задание 13

text = "Это пример строки (внутренний текст) для задания"

start = text.find('(')
end = text.find(')')

result = text[start+1:end]

print("Символы внутри скобок:", result)