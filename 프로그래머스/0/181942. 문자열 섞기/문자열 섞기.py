def solution(str1, str2):
    res = ''.join([str1[i] + str2[i] for i in range(len(str1))])
    return res