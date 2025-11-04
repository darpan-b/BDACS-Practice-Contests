#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    n = len(arr)
    if max(arr) <= 0:
        return [max(arr), max(arr)]
    subarrmax = 0
    cur = 0
    totmax = 0
    for i in range(n):
        if arr[i] >= 0:
            totmax += arr[i]
        cur += arr[i]
        subarrmax = max(subarrmax, cur)
        cur = max(cur, 0)
    return [subarrmax, totmax]    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
