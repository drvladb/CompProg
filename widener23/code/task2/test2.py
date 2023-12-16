import time
import math


def soln():
    a = int(input(": "))
    y = (a*a - a) % (10**math.ceil(math.log10(a))) == 0
    print("automorphic" if y else "not automorphic")


if __name__ == "__main__":
    soln()
