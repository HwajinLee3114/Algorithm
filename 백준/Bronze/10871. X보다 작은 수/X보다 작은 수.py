import sys
input = sys.stdin.readline
n, x = map(int, input().split())
a = input().split()

print(' '.join(num for num in a if int(num) < x))