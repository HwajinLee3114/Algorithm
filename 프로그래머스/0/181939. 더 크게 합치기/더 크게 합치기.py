def solution(a, b):
    tmp1 = f'{a}{b}'
    tmp2 = f'{b}{a}'
    return int(tmp1 if tmp1 > tmp2 else tmp2)