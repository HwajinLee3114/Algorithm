import sys
input = sys.stdin.readline
n, x, k = map(int, input().split())
cups = [0] * (n + 1)
cups[x] = 1

for _ in range(k):
    a, b = map(int, input().split())
    cups[a], cups[b] = cups[b], cups[a]

print(cups.index(1))