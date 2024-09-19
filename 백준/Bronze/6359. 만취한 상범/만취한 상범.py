t = int(input())
for i in range(t):
    n = int(input())
    rooms = [0] * (n + 1)
    for j in range(2, n + 1):
        for k in range(j, n + 1, j):
            if rooms[k] == 0: rooms[k] = 1
            else: rooms[k] = 0
    print(rooms[1:].count(0))