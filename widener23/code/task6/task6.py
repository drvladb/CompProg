import time
import math

def valid(arr,ind,m):
    return (arr[ind]//m) - (arr[ind-1]//m) <= 1

def newday(arr,ind,m):
    return (arr[ind] // m) - (arr[ind-1] // m) == 1
def soln():
    i1 = input().split()
    i2 = input().split()
    n = int(i1[0])
    m = int(i1[1])
    a = list(map(int,i2))
    d = {}

    for t in range(m):
        cs = 1
        best = 1
        for i in range(len(a)):
            a[i] += 1
        for i in range (1,len(a)):
            if (valid(a,i,m)):
                if (newday(a,i,m)):
                    cs += 1
            else:
                cs = 1
            if cs >= best:
                if cs in d.keys():
                    if (t+1)%m not in d[cs]:
                        d[cs].append((t+1)%m )
                else:
                    d[cs] = [(t+1)%m ]

    print(max(d.keys()))
    print(d[max(d.keys())])



if __name__ == "__main__":
    soln()
