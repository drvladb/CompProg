import time
import math


def soln():
    s = (input(": ")).lower()
    curMax=0
    curC=0
    a = ['a','e','i','o','u']
    for i in range(0,len(s)-1):
        if s[i] in a and s[i+1] in a:
            curC+=1

        if curC > curMax:
            curMax=curC
    print(curMax)




if __name__ == "__main__":
    soln()
