a = b = 100
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    if x > y: b -= x
    elif x < y: a -= y
print(a)
print(b)