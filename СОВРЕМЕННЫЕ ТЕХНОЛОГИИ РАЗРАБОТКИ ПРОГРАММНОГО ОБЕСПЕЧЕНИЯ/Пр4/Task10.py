#Бондаренков Ум-252 Практика 4
#Задание 10

n = int(input("Количество чисел: "))
k = int(input("С какого числа начать?: "))
s = 0
a = 0
b = 1
for i in range(1, k + n):
    if(i >= k):
        print(a, end=" ")
        s+=a
    a,b = b,a + b
print('\nCумма:', s)