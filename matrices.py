import numpy as np
   
def grid(n):
    if float(n**0.5).is_integer():
        length = int(n**0.5)
    else:
        length = int(np.floor(n**0.5))

    array = np.random.randint(10, size=(length, length))
    print(n-length)
        # for _ in range(n-(n**0.5)):
        #     pass
    print(array)

def main():
    grid(5)


if __name__ == "__main__":
    main()