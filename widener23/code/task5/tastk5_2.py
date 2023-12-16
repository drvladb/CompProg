import time
import math


def soln():
    n = int(input())
    m = int(input())
    c = int(input())

    best = 99999999999999
    best_m = []

    for M in range(0,math.ceil(n/m) + 1):
        delta = n - M*m
        a = M*m+c*(delta//c)
        if (abs(a-n) < best):
            best = abs(a-n)
            best_m = [(M,delta//c)]
        if (abs(a-n) == best):
            best_m.append((M,delta//c))
        a = M * m + c * math.ceil(delta/c)
        if (abs(a - n) < best):
            best = abs(a - n)
            best_m = [(M, math.ceil(delta/c))]
        if (abs(a - n) == best):
            best_m.append((M, math.ceil(delta/c)))

    for i in best_m:
        if not (i[0] < 0 or i[1] < 0): print(i)



if __name__ == "__main__":
    soln()
