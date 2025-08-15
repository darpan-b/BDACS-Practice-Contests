# ------------------- fast io --------------------
import os
import sys
from io import BytesIO, IOBase
 
BUFSIZE = 8192
 
 
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break 
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
# ------------------- fast io --------------------

# importing priority queue
import heapq




def shortestReach(n, adj, s):
    # Write your code here
    INF = 1e18
    dist = [INF for i in range(n)]
    dist[s] = 0
    to_process = []
    heapq.heappush(to_process, (dist[s],s))
    while to_process:
        curdist,curnode = heapq.heappop(to_process)
        if curdist != dist[curnode]:
            continue
        for node,d in adj[curnode]:
            if dist[node] > dist[curnode]+d:
                dist[node] = dist[curnode]+d
                heapq.heappush(to_process, (dist[node],node))
    dist = [-1 if dist[i] == 1e18 else dist[i] for i in range(n)]
    dist.pop(s)
    return dist
    



test = int(input())
for _ in range(test):

    n, m = map(int, input().split())

    # declares a double dimensional array of size n
    adj = [[] for i in range(n)]
    
    edges = {}
    
    for i in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        if u > v:
            u,v = v,u
        if (u,v) in edges:
            edges[(u,v)] = min(edges[(u,v)],w)
        else:
            edges[(u,v)] = w
    
    for u,v in edges:
        # appending each node as a tuple of (node number, edge weight)
        w = edges[(u,v)]
        adj[u].append((v, w))
        adj[v].append((u, w))

    s = int(input())-1
    answer = shortestReach(n,adj,s)
    print(*answer)
