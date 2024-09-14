n, m = map(int, input().split())
_tmp = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i, j + 1):
        _tmp[idx - 1] = k
print(*_tmp)