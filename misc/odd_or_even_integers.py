import numpy as np
from timeit import timeit

def odd_or_even_bin(num: int):
    if bin(num)[-1] == "1":
        return "odd"
    else:
        return "even"


def odd_or_even_std(num: int):
    if num % 2 == 1:
        return "odd"
    else:
        return "even"

def main():
    input = np.arange(0, 10_000_000, 1)
    bin_time = timeit(lambda: np.vectorize(odd_or_even_bin)(input), number=1)
    std_time = timeit(lambda: np.vectorize(odd_or_even_std)(input), number=1)
    print(f"Binary Time: {bin_time}")
    print(f"Standard Time: {std_time}")

if __name__ == "__main__":
    main()