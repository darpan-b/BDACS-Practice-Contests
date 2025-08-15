#!/bin/python3

import math
import os
import random
import re
import sys

ans = 0

def dfs(node, par, adj, compsz):
    global ans
    compsz[node] = 1
    for u in adj[node]:
        if u != par:
            dfs(u,node,adj,compsz)
            compsz[node] += compsz[u]
    if compsz[node] % 2 == 0:
        ans += 1

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    global ans
    compsz = [0 for i in range(t_nodes)]
    adj = [[] for i in range(t_nodes)]
    for i in range(t_edges):
        adj[t_from[i]-1].append(t_to[i]-1)
        adj[t_to[i]-1].append(t_from[i]-1)
    dfs(0,-1,adj,compsz)
    return ans-1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
