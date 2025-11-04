#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    pq = []
    for e in A:
        heapq.heappush(pq, (e,e))
    ans = 0
    while pq:
        ele, _ = heapq.heappop(pq)
        if ele >= k:
            return ans
        if not pq:
            return -1
        ele2, _ = heapq.heappop(pq)
        newele = ele + 2*ele2
        heapq.heappush(pq, (newele,newele))
        ans += 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
