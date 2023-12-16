import time
import math


def check(count,a):
    #print("ck", count, a)
    for i in range(count,len(a)):
        if a[i]>=0:
            return False
    return True


    pass
def soln():
    goal = int(input(": "))
    miles = int(input(": "))
    cables = int(input(": "))

    a= [goal]
    k = [ [ 0,0]  ]
    ks = set()
    counter = 0
    while not check(counter,a):



        kCopyA = k[counter][:]
        kCopyA[0]+=1
        kCopyB = k[counter][:]
        kCopyB[1]+=1

        if tuple(kCopyA) not in ks:
            a+=[a[counter]-miles]
            k.append(k[counter][:])
            #print(k)
            k[-1][0]+=1
            ks.add(tuple(k[-1][:]))

        if tuple(kCopyB) not in ks:

            a += [a[counter] - cables]
            k.append(k[counter][:])


           # print(k)

            k[-1][1] += 1
            ks.add(tuple(k[-1][:]))
        counter+=1


    best = 99999999999999999999999


    s = set()

    for x in range(len(a)):

        if abs(a[x])<best:

            best = abs(a[x])
            s = set()


        if abs(a[x])==best:
            s.add(tuple(k[x]))
    print(s)




if __name__ == "__main__":
    soln()
