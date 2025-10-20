#Бондаренков Ум-252 Практика 4
#Задание 8

n=int(input("Введите натуральное число меньше 10: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end='')
    print('')