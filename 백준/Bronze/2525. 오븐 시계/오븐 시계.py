a, b = map(int, input().split())
c = int(input())

hour = a + ((b + c) // 60)
min = (b + c) % 60
print(hour - 24 if hour >= 24 else hour, min)