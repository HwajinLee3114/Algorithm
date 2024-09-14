import sys
input = sys.stdin.readline
_tmp = list(range(1, 31))
for _ in range(28):
    _tmp.remove(int(input()))
print(min(_tmp))
print(max(_tmp))