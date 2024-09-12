a, b = map(int, input().split())
c = int(input())

hour = (a + ((b + c) // 60)) % 24
min = (b + c) % 60
print(hour, min)