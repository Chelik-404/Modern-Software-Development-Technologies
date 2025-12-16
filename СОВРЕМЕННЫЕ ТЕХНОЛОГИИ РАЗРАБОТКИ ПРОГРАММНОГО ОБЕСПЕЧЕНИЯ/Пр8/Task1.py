#Бондаренков Ум-252 Лабораторная работа 8
#Задание 1
#Вариант 3

A = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

n = len(A)
flag = True

for i in range(n):
    for j in range(n):
        if A[i][j] != A[j][i]:
            flag = False

if flag:
    print("Матрица симметрична")
else:
    print("Матрица не симметрична")