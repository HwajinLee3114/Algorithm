import sys
input = sys.stdin.readline
c = int(input())
n = 1

while c != 1:
    n += 1
    if not c % 2:
        c = c // 2
    else:
        c = 3 * c + 1
print(n)