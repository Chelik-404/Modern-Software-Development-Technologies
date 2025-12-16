#Бондаренков Ум-252 Лабораторная работа 9
#Задание 2
#Вариант 3 

def print_odd():
    x = int(input())
    if x == 0:
        return
    print(x)
    x = int(input())
    if x == 0:
        return
    print_odd()

print_odd()