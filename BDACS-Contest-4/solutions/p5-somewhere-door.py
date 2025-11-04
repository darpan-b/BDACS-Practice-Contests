# Enter your code here. Read input from STDIN. Print output to STDOUT

t1, t2 = map(int, input().split())
n = int(input())
s = list(map(int, input().split()))

s.sort()

# Find the first index i such that s[i+1] > t1
i = 0
while i + 1 < len(s) and s[i + 1] <= t1:
    i += 1

# Find the last index j such that s[j-1] < t2
j = len(s) - 1
while j - 1 >= 0 and s[j - 1] >= t2:
    j -= 1

# Print the difference
print(s[j] - s[i] + 1)
