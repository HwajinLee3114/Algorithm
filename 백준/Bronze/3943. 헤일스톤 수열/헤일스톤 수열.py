import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    tmp = [n]

    while n != 1:
        n = n // 2 if not n % 2 else n * 3 + 1
        tmp.append(n)

    print(max(tmp))