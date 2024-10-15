import sys
input = sys.stdin.readline

def switch_func(idx):
    status[idx] = 0 if status[idx] == 1 else 1
    return

n = int(input())
status = [0] + list(map(int, input().split()))
st = int(input())

for _ in range(st):
    s, num = map(int, input().split())
    if s == 1:
        for i in range(num, n + 1, num):
            switch_func(i)
    elif s == 2:
        switch_func(num)
        for i in range(n // 2):
            if num + i > n or num - i < 1: break
            if status[num + i] == status[num - i]:
                switch_func(num + i)
                switch_func(num - i)
            else: break

for i in range(1, len(status), 20):
    print(*status[i:i + 20])