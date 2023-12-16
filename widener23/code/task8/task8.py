import time
import math


def soln():
    h = input().split(" ")
    A = [c for c in h[0].upper()]
    B = [c for c in h[1].upper()]
    BO = B[:]

    for c in B:
        if c not in A:
            print("NO")
            return

    s = []
    for c in A[::-1]:
        if c in B:
            s = [c]+s
            B.remove(c)
    print("YES" if s == BO else "NO")



if __name__ == "__main__":
    soln()
