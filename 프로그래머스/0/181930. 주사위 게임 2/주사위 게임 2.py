def calc(a, b, c, n):
    tot = 1
    for i in range(1, n + 1):
        tot *= (a ** i + b ** i + c ** i)
    return tot

def solution(a, b, c):
    if a != b and a != c and b != c:
        return calc(a, b, c, 1)
    elif a == b == c:
        return calc(a, b, c, 3)
    else:
        return calc(a, b, c, 2)