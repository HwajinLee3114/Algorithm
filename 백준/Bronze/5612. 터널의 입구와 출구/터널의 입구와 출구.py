import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
maxCnt = m

for i in range(n):
    a, b = map(int, input().split())
    m = m + a - b

    if m < 0:
        maxCnt = 0
        break
    else:
        maxCnt = max(m, maxCnt)
print(maxCnt)