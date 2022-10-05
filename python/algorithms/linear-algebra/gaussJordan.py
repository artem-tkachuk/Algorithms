import numpy as np
import random

def gaussJordan(a):

    # if not isSquare(a):   #TODO fix
    #     return False

    m, n = len(a), len(a[0]) - 1  #number of rows and columns (without the values column)
    first_non_zero_row, first_non_zero_col = findNonZero(a, m, n)

    if first_non_zero_col == -1:  # zero matrix
        return False
    if a[0][first_non_zero_col] == 0:
        a = swapRows(a, n, 0, first_non_zero_row)

    for i in range(m):
        a = divideRow(a, n, row=i, col=first_non_zero_col + i)
        a = subtractRows(a, n, m, row=i, col=first_non_zero_col + i)

    for i in range (0, m):
        a = subtractRowsBack(a, n, m, first_non_zero_col, row=m - i, col=n - i)

    for row in a:
        print(row)

    # for k in range(n - 1, 0):


    #Выбирают первый слева столбец матрицы, в котором есть хоть одно отличное от нуля значение.
    # Если самое верхнее число в этом столбце ноль, то меняют всю первую строку матрицы с другой строкой матрицы, где в этой колонке нет нуля.
    # Все элементы первой строки делят на верхний элемент выбранного столбца.
    # Из оставшихся строк вычитают первую строку, умноженную на первый элемент соответствующей строки, с целью получить первым элементом каждой строки (кроме первой) ноль.
    # Далее проводят такую же процедуру с матрицей, получающейся из исходной матрицы после вычёркивания первой строки и первого столбца.
    # После повторения этой процедуры n − 1 раз получают верхнюю треугольную матрицу
    # Вычитают из предпоследней строки последнюю строку, умноженную на соответствующий коэффициент, с тем, чтобы в предпоследней строке осталась только 1 на главной диагонали.
    # Повторяют предыдущий шаг для последующих строк. В итоге получают единичную матрицу и решение на месте свободного вектора (с ним необходимо проводить все те же преобразования).

def divideRow(a, n, row, col):
    first = a[row][col]
    for i in range(col, n + 1):
        a[row][i] /= first
    return a


def subtractRowsBack(a, n, m, first_non_zero_col, row, col):
    for i in range(0, row - 1):
        first = a[m - i - 1][col]
        for j in range(first_non_zero_col, n + 1):
            a[i][j] -= a[row][j] * first
    return a

def subtractRows(a, n, m, row, col):
    for i in range(row + 1, m):
        first = a[i][col]
        for j in range(col, n + 1):
            a[i][j] -= a[row][j] * first
    return a

def swapRows(a, n, i, j):
    for k in range(n + 1):
        a[i][k], a[j][k] = a[j][k], a[i][k]
    return a

#the index of the first non-zero column from the left
def findNonZero(a, m, n):
    for j in range(n):
        for i in range(m):
            if a[i][j] != 0:  # found a non-zero column
                return (i, j)
    return (-1, -1)

 # a matrix is square and 2-dim
def isSquare(a):
    return len(a) + 1 == len(a[0]) # 2 dim?


def main():
    a = [
            [1, 4, 2, 3],
            [2, 0, 5, 6],
            [0, 0, 7, 8]
    ]

    gaussJordan(a)

if __name__ == '__main__':
    main()