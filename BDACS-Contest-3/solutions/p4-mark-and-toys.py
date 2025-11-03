# Solution by Ronak Sarkar


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Write your code here
    i,j=0,1
    count=1
    maxc=0
    prices.sort()
    while i<j<len(prices):
        if sum(prices[i:j+1])<k:
            j+=1
            count+=1
        elif sum(prices[i:j+1])>=k:
            i+=1
            maxc=max(count,maxc)

            count-=1
    
    return maxc

        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
