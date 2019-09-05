import numpy as np

def gaussJordan(a):

    # if not isSquare(a):   #TODO fix
    #     return False

    n = len(a)  #number of rows

    for k in range(n):
        first_non_zero_row, first_non_zero_col = findNonZero(a, k, n)

        if first_non_zero_col == -1:    #zero matrix
            break

        if a[k][first_non_zero_col] == 0:
            a = swapRows(a, n, k, first_non_zero_row)   #TODO scale?, debug?

        first = a[k][first_non_zero_col]
        for i in range(k, n + 1):
            a[k][i] = a[k][i] / first


        for i in range(k + 1, n):
            first = a[i][first_non_zero_col]
            for j in range(k, n + 1):
                a[i][j] -= a[first_non_zero_row][j] * first

    for row in a:
        print(row)

    for k in range(n - 1, 0):

    #Выбирают первый слева столбец матрицы, в котором есть хоть одно отличное от нуля значение.
    # Если самое верхнее число в этом столбце ноль, то меняют всю первую строку матрицы с другой строкой матрицы, где в этой колонке нет нуля.
    # Все элементы первой строки делят на верхний элемент выбранного столбца.
    # Из оставшихся строк вычитают первую строку, умноженную на первый элемент соответствующей строки, с целью получить первым элементом каждой строки (кроме первой) ноль.
    # Далее проводят такую же процедуру с матрицей, получающейся из исходной матрицы после вычёркивания первой строки и первого столбца.
    # После повторения этой процедуры n − 1 раз получают верхнюю треугольную матрицу
    # Вычитают из предпоследней строки последнюю строку, умноженную на соответствующий коэффициент, с тем, чтобы в предпоследней строке осталась только 1 на главной диагонали.
    # Повторяют предыдущий шаг для последующих строк. В итоге получают единичную матрицу и решение на месте свободного вектора (с ним необходимо проводить все те же преобразования).

def swapRows(a, n, i, j):
    for k in range(n + 1):
        a[i][k], a[j][k] = a[j][k], a[i][k]
    return a

#the index of the first non-zero column from the left
def findNonZero(a, m, n):
    for j in range(m, n):
        for i in range(m, n):
            if a[i][j] != 0:    #found a non-zero column
                return (i, j)
    return (-1, -1)

 # a matrix is square and 2-dim
def isSquare(a):
    return len(a) + 1 == len(a[0]) # 2 dim?


def main():
    a = [[1, 1, 1, 3],
         [2, 3, 7, 0],
         [1, 3, -2, 17]]
    print(gaussJordan(a))

if __name__ == '__main__':
    main()