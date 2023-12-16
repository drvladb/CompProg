import time
import math


def soln():
    a = input().split(" ")
    a = list(map(int, a))
    n = a[0] // a[1]
    o = a[0] - n * a[1]
    c = n * a[2] / 8
    print(n,o,c)


if __name__ == "__main__":
    soln()
