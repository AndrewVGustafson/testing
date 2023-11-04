import matplotlib.pyplot as plt
import numpy as np
import timeit

def linear(n):
    array = []
    for i in range(n):
        array.append(i)
    return array

def quadratic(n):
    array = []
    for i in range(n):
        for i in range(len(array)):
            pass
        array.append(i)
    return array


def get_points(n, func):
    timed = lambda x, func :timeit.timeit(lambda: func(x), number=10)
    x = np.array([i for i in range(n)])
    y = np.array([timed(i, func) for i in range(n)])
    return [x, y]

points1 = get_points(1000, linear)
points2 = get_points(1000, quadratic)

plt.plot(points1[0], points1[1])
plt.plot(points2[0], points2[1])
plt.show()
