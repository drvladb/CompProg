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
    inp = int(input())

    mini_arr = []
    for i in range(inp):

        mini_inp = input()

        mini_arr.append(mini_inp.split(" "))
    data.append(mini_arr)

output = []


def dist(x,y):
    x=int(x)
    y=int(y)
    return (x**2 + y**2) **0.5
# DO PROCESSING HERE
for point in data:
    #print(data[0])
    arr = [dist(point[0][0],point[0][1])]
    
    for i in range(1,len(point)): # point1, point 2 ...
        dist_i = dist(point[i][0],point[i][1])

        for x in range(len(arr)):
            if arr[x] > dist_i:
                arr.insert(x,dist_i)
        
    

    output.append(arr);print(arr)


print("\n".join(output))
