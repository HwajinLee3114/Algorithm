import sys
input = sys.stdin.readline
n = int(input())
for idx in range(n):
    print(f'Case #{idx + 1}: {sum(map(int, input().split()))}')