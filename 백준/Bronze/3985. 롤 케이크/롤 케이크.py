import sys
input = sys.stdin.readline
L = int(input())
N = int(input())
cake = [0] * (L + 1)
exp = exp_val = 0   # 기대
real = real_val = 0 # 실제
for i in range(1, N + 1):
    p, k = map(int, input().split())
    tmp = k - p + 1
    if exp_val < tmp:
        exp_val, exp = tmp, i
    elif exp_val == tmp and exp > i:
        exp = i
    for j in range(p, k + 1):
        if not cake[j]: cake[j] = i
for i in range(1, N + 1):
    tmp = cake.count(i)
    if real_val < tmp:
        real_val, real = tmp, i
    elif real_val == tmp and real > i:
        real = i
print(exp)
print(real)