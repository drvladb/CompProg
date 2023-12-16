import time
import math
import itertools

def soln():
    n = int(input(": "))
    a = input(": ")


    arr = [int(x) for x in a.split(" ")]

    tripletCount = 0

    for poss in list(itertools.combinations(arr,3)):
        if math.gcd(poss[0],poss[1],poss[2])==1:
            if (1<=poss[0] and poss[0]<=poss[1] and poss[1]<=poss[2]):
                tripletCount+=1

    print(tripletCount)



if __name__ == "__main__":
    soln()
