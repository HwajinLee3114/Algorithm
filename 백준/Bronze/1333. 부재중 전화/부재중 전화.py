import sys
input = sys.stdin.readline
n, l, d = map(int, input().split())
res = 0
total = n * l + (n - 1) * 5
arr = [0] * total

for i in range(0, total, l + 5):
    for j in range(i, i + l):
        arr[j] = 1

while res < len(arr):
    if not arr[res]: break
    res += d

print(res)