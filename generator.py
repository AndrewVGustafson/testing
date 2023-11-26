def gen(n):
    x2 = 0
    x1 = 1
    yield x2
    yield x1

    for _ in range(2, n+1):
        yield x2 + x1
        x2, x1 = x1, x2 + x1

for value in gen(10):
    print(value)
