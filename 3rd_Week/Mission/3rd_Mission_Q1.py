import numpy as np
import random

arr1 = np.random.randn(5, 3)
arr2 = np.random.randn(3, 2)

dot = np.dot(arr1, arr2)

print(dot, dot.shape)