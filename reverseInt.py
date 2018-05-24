#! python3
# reverseInt.py - reverse a given interger

import timeit

def reverse(x):
    if x >= 0:
        r = int(str(x)[::-1])
    else:
        r = -1 * int(str(x)[:0:-1])
    if r < -2**31 or r > 2**31 -1:
        return 0
    else:
        return r

def reverse1(x):
    s = str(x)
    r = ''
    for i in range(1, len(s) + 1):
        r += s[-i]
    if r[-1] == '-':
        r = '-' + r[:-1]
    r = int(r)
    if r < -2 ** 31 or r > 2 ** 31 - 1:
        return 0
    else:
        return r

def main():
    print(timeit.timeit('reverse(-123)', globals=globals()))
    print(timeit.timeit('reverse1(-123)', globals=globals()))

if __name__ == "__main__":
    main()
