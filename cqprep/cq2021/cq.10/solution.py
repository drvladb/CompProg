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
    data.append(inp)

output = []

# DO PROCESSING HERE
for point in data:
    arr = point.split(" ")
    if arr[0] == "formatHeight":
        output.append(arr[1]+"'"+arr[2]+'"')
    if arr[0] == "formatDate":
        output.append("0"*(4-len(arr[1]))+arr[1]+"0"*(2-len(arr[2]))+arr[2]+"0"*(2-len(arr[3]))+arr[3])
    if arr[0] == "concatenate":
        output.append(",".join(arr[1:]))

print("\n".join(output))
