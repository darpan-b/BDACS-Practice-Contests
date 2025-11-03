# Solution by Partha Mete


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
        ls=rs=0
        n=len(arr)
        for i in range(n):
            if i==0:
                if arr[i+1:]:
                    rs=sum(arr[i+1:])
            else:
                ls+=arr[i-1]
                rs-=arr[i]
            if ls==rs:
                return 'YES'
        return 'NO'  


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
