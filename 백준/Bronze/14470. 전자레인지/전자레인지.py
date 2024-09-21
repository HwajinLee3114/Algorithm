import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
tot = 0
if a < 0:
    tot += (a * -1 * c) + d
    tot += b * e
else:
    tot += (b - a) * e
print(tot)