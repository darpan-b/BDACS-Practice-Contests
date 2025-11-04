n, t = map(int, input().split())
arr = list(map(int, input().split()))

freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1

ans = 0
for l in sorted(freq.keys()):
    r = t - l
    if l > r:
        break
    if l == r:
        cnt = freq[l]
        ans += (cnt * (cnt - 1)) // 2
    elif r in freq:
        ans += freq[l] * freq[r]

print(ans)
