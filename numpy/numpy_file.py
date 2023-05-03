# different between numpy and list in python
# list: slow, numpy: fast

import numpy as np
import sys

a = np.array([1, 2, 3], dtype='int8')
b = np.array([[1.0, 2.0, 3.0], [5.0, 3.0, 7.0]])

print(b)

# matrix must have same col
# b = np.array([[1.0, 2.0, 3.0], [5.0, 3.0]]) => this will error

# get dimension
print("Dimension matrix A:", a.ndim)  # 1 (row)
print("Dimension matrix B:", b.ndim)  # 2 (row)

# get shape
# (3,)   {a.shape[0] or a.shape[1] will error}
print("Shape matrix A:", a.shape)
print("Shape matrix B:", b.shape)  # (2, 3) {b.shape[0] or b.shape[1]}

# get Type
print("Type", b.dtype)  # float64
