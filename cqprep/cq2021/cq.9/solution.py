from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN, getcontext
from math import floor

getcontext().prec = 15

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
    data.append(float(inp))

output = []

denoms = [100, 50, 20, 10, 5, 2, 1, .25, .1, .05, .01]

# DO PROCESSING HERE
for point in data:
    val = point
    out = []
    for denom in denoms:
        v = int(floor((val + 0.001) / denom))
        out.append(str(v))
        val -= v * denom
        # print(val, end=" ")
    # print()
    output.append("".join(out))

print("\n".join(output))
