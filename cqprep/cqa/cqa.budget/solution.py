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
    r = int(input())
    # print(input().split(" "))
    budget = input()
    budget = list(map(float, budget.split(" ")))
    actual = input()
    actual = list(map(float, actual.split(" ")))
    data.append([budget, actual])

output = []

# DO PROCESSING HERE
for point in data:
    # print(point)
    c = 0
    for i in range(len(point[0])):
        c += (point[1][i] - point[0][i])
    output.append(round_advanced(c / len(point[0]), 2))

print("\n".join([str(a) for a in output]))
