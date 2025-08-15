#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    # Write your code here
    adj = [[] for i in range(n)]
    for e in edges:
        adj[e[0]-1].append(e[1]-1)
        adj[e[1]-1].append(e[0]-1)
    q = []
    dist = [1e18 for i in range(n)]
    s -= 1
    dist[s] = 0
    q.append(s)
    while q:
        curnode = q.pop(0)
        for neigh in adj[curnode]:
            if dist[neigh] > dist[curnode]+6:
                dist[neigh] = dist[curnode]+6
                q.append(neigh)
    ans = []
    for i in range(n):
        if i == s:
            continue
        elif dist[i] == 1e18:
            ans.append(-1)
        else:
            ans.append(dist[i])
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
