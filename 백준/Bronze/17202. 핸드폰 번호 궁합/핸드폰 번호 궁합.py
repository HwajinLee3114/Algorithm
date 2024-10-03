import sys
input = sys.stdin.readline
a = list(input())
b = list(input())
arr = []
for i in range(8):
    arr.append(int(a[i]))
    arr.append(int(b[i]))

while len(arr) != 2:
    tmp = []
    for i in range(len(arr) -1):
        tmp.append((arr[i] + arr[i + 1]) % 10)
    arr = tmp

print(*arr, sep='')