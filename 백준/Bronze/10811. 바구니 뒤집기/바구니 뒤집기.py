import sys
input = sys.stdin.readline
n, m = map(int, input().split())
_arr = list(range(1, n + 1))
for _ in range(m):
    i, j = map(int, input().split())
    _tmp = _arr[i - 1:j]
    _tmp.reverse()
    _arr[i - 1:j] = _tmp
print(*_arr)