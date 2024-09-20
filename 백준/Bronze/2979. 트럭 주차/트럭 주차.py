import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())
parking = [0] * 101
total = 0
for _ in range(3):
    arr, dep = map(int, input().split())
    for i in range(arr, dep):
        parking[i] += 1

for cnt in parking:
    if cnt == 1:
        total += a
    elif cnt == 2:
        total += 2 * b
    elif cnt == 3:
        total += 3 * c
print(total)