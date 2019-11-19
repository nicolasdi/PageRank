import numpy as np

'''
Read a matrix from a .txt file and returns it in a numpy array
'''
def buildmatrix(filename):
    file_obj = open(filename)
    columns = int(file_obj.readline())
    matrix = []

    for i in range(0, columns):

        # numbers of characters to read
        row = file_obj.readline(columns*2 - 1)
        row = list(map(int, row.split(sep = ",")))

        # pass \n character
        file_obj.readline(1)

        matrix.append(row)

    return np.array(matrix)
