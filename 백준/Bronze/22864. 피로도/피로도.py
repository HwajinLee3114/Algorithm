import sys
input = sys.stdin.readline
a, b, c, m = map(int, input().split())
fl = 0
work = 0

for h in range(1, 25):
    max_fl = fl + a
    if max_fl <= m:
        fl += a
        work += b
    else:
        tmp = fl - c
        fl = 0 if tmp <  0 else tmp

print(work)