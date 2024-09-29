import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split(',')))

for _ in range(k):
    tmp = [a[idx + 1] - a[idx] for idx in range(len(a) - 1)]
    a = tmp
print(*a, sep=',')