# Solution by Arnab Singha


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    h=[0]*26
    for i in s:
        if i!=" ":
            h[ord(i.upper())-65]=1
        
    if sum(h)==26:
        return 'pangram'
    else:
        return 'not pangram'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
