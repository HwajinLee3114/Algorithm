import sys
input = sys.stdin.readline
n, m, l = map(int, input().split())
status = [0] * (n + 1)
cnt = 0
status[1] = i = 1

while status[i] != m:
    if status[i] % 2 == 1:  # 홀수
        i = (i + l) % n
    else:                   # 짝수
        i = (i - l) % n
    status[i] += 1
    cnt += 1

print(cnt)