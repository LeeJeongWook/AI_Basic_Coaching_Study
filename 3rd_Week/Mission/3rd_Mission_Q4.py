import numpy as np
import random

arr1 = np.array([[5,7], [9,11]], float)
arr2 = np.array([[2,4], [6,8]], float)

concat_1 = np.concatenate((arr1, arr2), axis = 0)     # TODO axis 0
concat_2 = np.concatenate((arr1, arr2), axis = 1)     # TODO axis 1

# print(concat_1)
# print(concat_2)
# -------------------------3rd_Mission_Q3-------------------------

beta_gd = np.random.rand(1)
bias = np.random.rand(1)

print(beta_gd, bias)