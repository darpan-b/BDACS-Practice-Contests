#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    # Write your code here
    n = len(h)
    nse = [n for i in range(n)]
    pse = [-1 for i in range(n)]
    stk = []
    for i in range(n):
        while stk and h[stk[-1]] > h[i]:
            nse[stk[-1]] = i
            stk.pop()
        stk.append(i)
    stk = []
    for i in range(n-1,-1,-1):
        while stk and h[stk[-1]] > h[i]:
            pse[stk[-1]] = i
            stk.pop()
        stk.append(i)
    ans = 0
    for i in range(n):
        ans = max(ans, h[i]*(nse[i]-pse[i]-1))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
