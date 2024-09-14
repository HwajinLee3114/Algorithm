def solution(a, d, included):
    result = 0

    for idx, val in enumerate(included):
        if val:
            result += a + (idx * d)
    return result