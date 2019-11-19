# Idea de algoritmo
# Leer gráfica
# Obtener su matriz
import numpy as np

a = np.array([[0, 0, 1, 0, 0], [1/3, 0, 1/3, 1/3, 0], [0, 0, 0, 1/2, 1/2], [1/2, 0, 1/2, 0, 0], [0, 1/2, 1/2, 0, 0] ])
b = a
c = np.matmul(a,b)
print(c)
