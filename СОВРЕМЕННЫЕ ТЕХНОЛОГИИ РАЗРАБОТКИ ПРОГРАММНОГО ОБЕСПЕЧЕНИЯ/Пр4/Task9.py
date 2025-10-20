#Бондаренков Ум-252 Практика 4
#Задание 9

n=int(input("Введите число: "))
s=1
a=0
b=1
print(a,b,end=" ")
for i in range(n-2):
   v=b
   b+=a
   a=v
   print(b,end=" ")
   s+=b
print('\nCумма:', s)