from asyncio import get_child_watcher
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
# -------------------------3rd_Mission_Q4-------------------------

learning_rate = 0.01

for i in range(1000):
    pred = (x_train * beta_gd) + bias
    error = ((pred - y_train) ** 2).mean()

    gd_w = ((pred - y_train) * 2 * x_train).mean()
    gd_b = ((pred - y_train) * 2).mean()

    beta_gd -= learning_rate * gd_w
    bias -= learning_rate * gd_b

    if i % 100 == 0:
        print('Epoch({:10d} error: {:10f}, beta_gd: {:10f}, bias: {:10f}'.format(i, error, beta_gd.item(), bias.item()))