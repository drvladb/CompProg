import time
import math


def soln():
    tally = {}
    candidates = input().split(" ")
    for cand in candidates:
        tally[cand] = {k: 0 for k in candidates}
    while True:
        vote = input()
        if vote == ".":
            break
        vote = vote.split(" ")
        notin = []
        for cand in candidates:
            if cand not in vote:
                notin.append(cand)
        for i, cand in enumerate(vote):
            won = vote[i + 1:] + notin
            for z in won:
                tally[cand][z] += 1
    print(tally)
    any = False
    for cand in candidates:
        fail = False
        for opp in candidates:
            if opp == cand:
                continue
            if tally[cand][opp] <= tally[opp][cand]:
                fail = True
                break
        if not fail:
            print(cand)
            # should be no more
            any = True
    if not any:
        print(0)



if __name__ == "__main__":
    soln()
