from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN
from math import floor

##### FUNCTIONS ######

# standard rounding
# n - number to round
# d - decimal places
def round_standard(n, d):
    return floor(n*(10**d)+0.5)/10**d


# advanced rounding (when needed, like with "are we on budget")
# n - number to round
# d - decimal places
# m - rounding mode
def round_advanced(n, d, m = ROUND_HALF_UP):
    # quantize takes 0.1, 0.01 etc.
    return Decimal(n).quantize(Decimal(str(10**-d)), rounding=m)

# get ascii position of a character (0 (a) - 25 (z))
def ascii_pos(l, cap = True):
    return ord(l) - ord("A" if cap else "a")
    
##### FUNCTION TESTS ######
# print(ascii_pos("z", False))
# print(round_advanced(1.5, 0))


######## INPUT ##########
num_lines = int(input())
data = []
for n in range(num_lines):
    # process the line here, append to data
    inp = input()
    data.append(inp.split(" "))

output = []

def getScore(score):
    if score==-15:
        return 2
    if score == -14:
        return 1
    if score==-13:
        return 2
    if score==-12:
        return 1
    if score==-11:
        return 2
    if score==-10:
        return 2
    if score==-9:
        return 1
    if score==-8:
        return 2
    if score==-7:
        return 1
    if score==-6:
        return 1
    if score==-5:
        return 2
    if score==-4:
        return 2
    if score==-3:
        return 1
    if score==-2:
        return 2
    if score==-1:
        return 1
    if score==0:
        return 1
    if score==1:
        return 2
    if score==2:
        return 1
    if score==3:
        return 1
    if score==4:
        return 1
    if score==5:
        return 2
    if score==6:
        return 1
    if score==7:
        return 1
    if score==8:
        return 1
    if score==9:
        return 1
    if score==10:
        return 1
    if score==11:
        return 1
    if score==12:
        return 2
    return 1
# DO PROCESSING HERE
for point in data:
    score = int(point[0]) - int(point[1])

    output.append(str(getScore(score)))

print("\n".join(output))
