#Бондаренков Ум-252 Практика 5
#Задание 12

text='На аллее расцвела сирень, звучала мелодия, и в воздухе витала лёгкая ностальгия.'

for i in '.,!?—':
    text = text.replace(i, '')

words = text.split()
results=[]
for word in words:
    if word[-1] == 'я':
        results.append(word)
print(' '.join(results))