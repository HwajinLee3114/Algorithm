import sys
input = sys.stdin.readline

n = int(input())
org = [i for i in range(n + 1)]

while len(org) > 2:
    tmp = []
    for i, v in enumerate(org):
        if not i % 2:  # 홀수 자리 지우기
            tmp.append(v)
            org = tmp
print(org[1])