import sys
input = sys.stdin.readline

k = int(input())
n = int(input())
sec = 210

for _ in range(n):
    t, z = input().split()
    sec -= int(t)

    if sec <= 0:
        print(k)
        break
    if z == 'T':
        k = (k + 1) % 9
        if k == 0:
            k += 1