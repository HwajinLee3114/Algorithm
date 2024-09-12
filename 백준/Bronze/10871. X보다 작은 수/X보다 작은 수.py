import sys
input = sys.stdin.readline
n, x = map(int, input().split())
a = input().split()
_tmp = []
for num in a:
    if int(num) < x: _tmp.append(num)
print(' '.join(_tmp))