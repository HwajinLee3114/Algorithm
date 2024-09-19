import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    rooms = [0] * (n + 1)   # 처음엔 다 열려 있어
    for j in range(2, n + 1):   # 라운드 돌기
        for k in range(j, n + 1, j): # j 배수 일때 처리
            if rooms[k] == 0: rooms[k] = 1
            else: rooms[k] = 0
    print(rooms[1:].count(0))