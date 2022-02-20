import numpy as np
import random

xy = np.array([[1., 2., 3., 4., 5., 6.], [10., 20., 30., 40., 50., 60.]])

x_train = xy[0]
y_train = xy[1]

# print(x_train, x_train.shape)
# print(y_train, y_train.shape)
# -------------------------3rd_Mission_Q3-------------------------

beta_gd = np.random.rand(1)
bias = np.random.rand(1)

print(beta_gd, bias)