import sys
input = sys.stdin.readline
balls = [0, 1, 2, 3]
changes = input().strip()
for v in changes:
    if v == 'A':
        balls[1], balls[2] = balls[2], balls[1]
    elif v == 'B':
        balls[2], balls[3] = balls[3], balls[2]
    elif v == 'C':
        balls[1], balls[3] = balls[3], balls[1]
print(balls.index(1))