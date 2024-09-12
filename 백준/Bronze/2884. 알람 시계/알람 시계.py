h, m = map(int, input().split())
if m < 45:  print(h - 1 if h > 0 else 23, m + 15)
else: print(h, m - 45)