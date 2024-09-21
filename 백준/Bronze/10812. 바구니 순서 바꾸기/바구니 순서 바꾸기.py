import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [i for i in range(n+1)]
for _ in range(m):
    begin, end, mid = map(int, input().split())
    arr = arr[:begin] + arr[mid:end + 1] + arr[begin:mid] + arr[end + 1:]
print(*arr[1:])