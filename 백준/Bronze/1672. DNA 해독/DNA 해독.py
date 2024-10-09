import sys
input = sys.stdin.readline

DNA = {
    'AA':'A',
    'AG':'C',
    'AC':'A',
    'AT':'G',
    'GA':'C',
    'GG':'G',
    'GC':'T',
    'GT':'A',
    'CA':'A',
    'CG':'T',
    'CC':'C',
    'CT':'G',
    'TA':'G',
    'TG':'A',
    'TC':'G',
    'TT':'T'
}

n = int(input())
arr = list(input().strip())

while len(arr) > 1:
    last = ''.join(arr[-2:])
    arr.pop()
    arr.pop()
    arr.append(DNA[last])

print(*arr)