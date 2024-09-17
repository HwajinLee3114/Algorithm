arr = list(i for i in range(21))
for _ in range(10):
    a, b = map(int, input().split())
    _tmp = arr[a: b + 1]
    _tmp.reverse()
    arr[a: b + 1] = _tmp
print(' '.join(map(str, arr[1:])))