#Бондаренков Ум-252 Лабораторная работа 8
#Задание 2
#Вариант 3 

A = [
    [1.5, 2.1, 3.3],
    [4.8, 0.2, 1.1],
    [2.4, 3.9, 0.5]
]

n = len(A)
m = len(A[0])

max_i = 0
max_j = 0

for i in range(n):
    for j in range(m):
        if A[i][j] > A[max_i][max_j]:
            max_i = i
            max_j = j

# меняем строки
A[0], A[max_i] = A[max_i], A[0]

# меняем столбцы
for i in range(n):
    A[i][0], A[i][max_j] = A[i][max_j], A[i][0]

print("Преобразованная матрица:")
for row in A:
    print(row)