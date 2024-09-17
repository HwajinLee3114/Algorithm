m = int(input())
_tmp = [0, 1, 2, 3]
for _ in range(m):
    x, y = map(int, input().split())
    _tmp[x], _tmp[y] = _tmp[y], _tmp[x]
print(_tmp.index(1))