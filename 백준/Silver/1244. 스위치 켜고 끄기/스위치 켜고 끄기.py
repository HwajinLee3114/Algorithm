import sys
input = sys.stdin.readline

n = int(input())
status = [0] + list(map(int, input().split()))
st = int(input())

for _ in range(st):
    s, num = map(int, input().split())
    if s == 1:
        for i in range(num, n + 1, num):
            status[i] = 0 if status[i] == 1 else 1
    elif s == 2:
        status[num] = 0 if status[num] == 1 else 1
        for i in range(n // 2):
            if num + i > n or num - i < 1: break
            if status[num + i] == status[num - i]:
                status[num + i] = 0 if status[num + i] == 1 else 1
                status[num - i] = 0 if status[num - i] == 1 else 1
            else: break

for i in range(1, len(status), 20):
    print(*status[i:i + 20])