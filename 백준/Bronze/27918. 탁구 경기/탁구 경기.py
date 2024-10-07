import sys
input = sys.stdin.readline
n = int(input())
x = 0
y = 0

for _ in range(n):
    win = input().strip()
    if win == 'D': x += 1
    else: y += 1
    if abs(x-y) == 2:
        break
print(f'{x}:{y}')