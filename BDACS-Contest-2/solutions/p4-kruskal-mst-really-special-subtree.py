#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def findroot(u, roots):
    if roots[u] == u:
        return u
    else:
        roots[u] = findroot(roots[u],roots)
        return roots[u]

def unite(u, v, roots, compsz):
    ru, rv = findroot(u,roots), findroot(v,roots)
    if ru == rv:
        return False
    else:
        if compsz[ru] < compsz[rv]:
            ru,rv = rv,ru
        compsz[ru] += compsz[rv]
        roots[rv] = ru
        return True
    
def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    roots = [i for i in range(g_nodes)]
    ranks = [0 for i in range(g_nodes)]
    edges = []
    for i in range(len(g_from)):
        edges.append((g_weight[i],g_from[i]-1,g_to[i]-1))
    edges.sort()
    ans = 0
    for i in range(len(edges)):
        if unite(edges[i][1], edges[i][2], roots, ranks):
            ans += edges[i][0]
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    fptr.write(str(res) + '\n')

    fptr.close()
