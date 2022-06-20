matrix = [[1, 0, 8],
         [3, 4, 1],
         [0, 4, 2]]


matrix_rotate =[list(a) for a in list(zip(*matrix))]

print('Транспонированная матрица\n', *matrix_rotate, sep = '\n') 