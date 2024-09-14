import sys
input = sys.stdin.readline
n, m = map(int, input().split())
_tmp = list(range(1, n + 1))
for _ in range(m):
    i, j = map(int, input().split())
    tmp_num = _tmp[i - 1]
    _tmp[i - 1] = _tmp[j - 1]
    _tmp[j - 1] = tmp_num
print(*_tmp)