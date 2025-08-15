#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def dfs(node, adj, vis):
    vis[node] = True
    for v in adj[node]:
        if not vis[v]:
            dfs(v, adj, vis)

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    adj = [[] for i in range(n)]
    for c in cities:
        adj[c[0]-1].append(c[1]-1)
        adj[c[1]-1].append(c[0]-1)
    vis = [False for i in range(n)]
    comps = 0
    for i in range(n):
        if not vis[i]:
            comps += 1
            compsz = 0
            dfs(i,adj,vis)
    ans = min(n*c_lib, comps*c_lib+c_road*(n-comps))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
