#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    stk = []
    for ch in s:
        if ch == "(":
            stk.append(1)
        elif ch == "{":
            stk.append(2)
        elif ch == "[":
            stk.append(3)
        elif ch == ")":
            if len(stk) == 0 or stk[-1] != 1:
                return "NO"
            else:
                stk.pop()
        elif ch == "}":
            if len(stk) == 0 or stk[-1] != 2:
                return "NO"
            else:
                stk.pop()
        elif ch == "]":
            if len(stk) == 0 or stk[-1] != 3:
                return "NO"
            else:
                stk.pop()
    if not stk:
        return "YES"
    else:
        return "NO" 
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
