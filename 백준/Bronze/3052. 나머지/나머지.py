import sys
input = sys.stdin.readline
_tmp = []
for _ in range(10):
    _tmp.append(int(input()) % 42)
print(len(set(_tmp)))