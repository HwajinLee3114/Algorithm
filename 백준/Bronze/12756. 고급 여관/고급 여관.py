import sys
input = sys.stdin.readline
a, b = map(int, input().split())
x, y = map(int, input().split())

while b > 0 and y > 0:
    b -= x
    y -= a

if b > 0: print('PLAYER A')
elif y > 0: print('PLAYER B')
else: print('DRAW')