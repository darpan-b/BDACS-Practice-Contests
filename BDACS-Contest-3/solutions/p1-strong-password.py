# Solution by Ronak Sarkar


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    count=0
    for i in password:
        if i in numbers:
            break
    else:
        count+=1
    for i in password:
        if i in lower_case:
            break
    else:
        count+=1
    for i in password:
        if i in upper_case:
            break
    else:
        count+=1
    for i in password:
        if i in special_characters:
            break
    else:
        count+=1
    return max(6-n,count) if 6-n<=6 else count
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
