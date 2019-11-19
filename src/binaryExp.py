import numpy as np

# Binary exponentiation (k x k) matrix
def binaryExpo(matrix, n):

    if (n == 1):
        return matrix

    elif (n % 2 == 0):
        b = binaryExpo(matrix, n/2)
        return np.matmul(b, b)

    # odd exponent
    b = binaryExpo(matrix, n - 1)
    return np.matmul(matrix, b )

#a = np.array([[0, 0, 1, 0, 0], [1/3, 0, 1/3, 1/3, 0], [0, 0, 0, 1/2, 1/2], [1/2, 0, 1/2, 0, 0], [0, 1/2, 1/2, 0, 0] ])

#print(binaryExpo(a, 3))
