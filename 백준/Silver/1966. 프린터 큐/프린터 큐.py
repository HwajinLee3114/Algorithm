import sys
input = sys.stdin.readline
a = int(input())
for _ in range(a):
    n, m = map(int, input().split())
    _docs = list(map(int, input().split()))
    _tmp = 1

    while _docs:
        if _docs[0] < max(_docs):
            _docs.append(_docs.pop(0))
        else:
            if m == 0: break
            _docs.pop(0)
            _tmp += 1

        m = m - 1 if m > 0 else len(_docs) -1
    print(_tmp)