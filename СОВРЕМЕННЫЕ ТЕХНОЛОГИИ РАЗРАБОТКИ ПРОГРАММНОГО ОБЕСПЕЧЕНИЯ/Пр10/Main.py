#Бондаренков Ум-252
#Лабораторная работа 10
import os
print(os.getcwd())


file = open('Bondarenkov_UM252_vvod.txt', 'r')

n = int(file.readline())

A = []
for i in range(n):
    row = list(map(int, file.readline().split()))
    A.append(row)

file.readline()

B = []
for i in range(n):
    row = list(map(float, file.readline().split()))
    B.append(row)

file.close()

#Task 1
flag = True
for i in range(n):
    for j in range(n):
        if A[i][j] != A[j][i]:
            flag = False

#Task 2
max_i = 0
max_j = 0

for i in range(n):
    for j in range(n):
        if B[i][j] > B[max_i][max_j]:
            max_i = i
            max_j = j


B[0], B[max_i] = B[max_i], B[0]


for i in range(n):
    B[i][0], B[i][max_j] = B[i][max_j], B[i][0]

#ВЫВОД 
file = open('Bondarenkov_UM252_vivod.txt', 'w',encoding='utf-8')

if flag:
    file.write("Матрица A симметрична\n")
else:
    file.write("Матрица A не симметрична\n")

file.write("Преобразованная матрица B:\n")
for row in B:
    file.write(' '.join(map(str, row)) + '\n')

file.close()