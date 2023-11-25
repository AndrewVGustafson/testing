import numpy as np
   
def grid(n):
    if float(n**0.5).is_integer():
        length = int(n**0.5)
        array = np.zeros((length, length), dtype=np.int8)

    else:
        length = int(np.floor(n**0.5))
        array = np.zeros((length+1, length), dtype=np.int8)



    # for row in range(n-length**2):
    #     array.
    print(array)

def main():
    grid(8)


if __name__ == "__main__":
    main()