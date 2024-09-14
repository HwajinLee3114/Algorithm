import sys
input = sys.stdin.readline
n, m = map(int, input().split())
_tmp = list(range(1, n + 1))
for _ in range(m):
    i, j = map(int, input().split())
    _tmp[i - 1], _tmp[j - 1] = _tmp[j - 1], _tmp[i - 1]
print(*_tmp)