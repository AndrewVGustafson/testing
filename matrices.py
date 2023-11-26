import numpy as np
   
def grid(n):
    if float(n**0.5).is_integer():
        length = int(n**0.5)
        array = np.ones((length, length), dtype=np.int8)

    else:
        length = int(np.floor(n**0.5))
        extra_cells = n-length**2
        extra_rows = int(np.ceil(extra_cells/length))
        print(f"matrix length: {length}")
        print(f"extra cells needed: {extra_cells}")
        print(f"extra rows needed: {extra_rows}")
        array = np.ones((length, length), dtype=np.int8)
        if extra_cells >= length:
            extra_rows = np.ones((extra_rows-1, length), dtype=np.int8)
            extra_cells -= length

        print(extra_rows)
        
        print()
        # extra_rows = np.vstack((extra_rows, [1 for _ in range(extra_cells)]))
        array = np.vstack((array, extra_rows))


    # for row in range(n-length**2):
    #     array.
    print(array)

def main():
    grid(13)


if __name__ == "__main__":
    main()