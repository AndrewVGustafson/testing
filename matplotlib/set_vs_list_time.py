from timeit import timeit
import matplotlib.pyplot as plt
import numpy as np

n = 1000

l = list(range(n))
s = set(range(n))

# finding value: set faster
timed_list = lambda n: timeit(f"{n}-1 in l", number=1, globals=globals())
timed_set = lambda n : timeit(f"{n}-1 in s", number=1, globals=globals())

# finding max value: equal times
# timed_list = lambda n: timeit(lambda: max(l), number=1, globals=globals())
# timed_set = lambda n : timeit(lambda: max(s), number=1, globals=globals())

x1 = np.array([i for i in range(n)])
y1 = np.array([timed_list(i) for i in range(n)])
x2 = np.array([i for i in range(n)])
y2 = np.array([timed_set(i) for i in range(n)])

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.title("Set vs List time complexity")
plt.xlabel("Size")
plt.ylabel("Time")
plt.show()