#Бондаренков Ум-252 Практика 4
#Задание 2

a=int(input("1 число: "))
b=int(input("2 число: "))
if(a<=b):
    while(a<=b):
        print(a)
        a+=1
else:
    while(a>=b):
        print(a)
        a-=1