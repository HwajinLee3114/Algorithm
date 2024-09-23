import sys
input = sys.stdin.readline
N, m, M, T, R = map(int, input().split())
totTime = excTime = 0
now = m
while excTime < N:
    if m + T > M: break
    if now + T <= M:
        excTime += 1
        now += T
    else:
        now = m if now - R < m else now - R
    totTime += 1
print(totTime if excTime == N else -1)