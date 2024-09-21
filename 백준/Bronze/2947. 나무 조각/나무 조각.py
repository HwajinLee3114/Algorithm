arr = list(map(int, input().split()))
while 1:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            print(*arr)
    if arr == [1, 2, 3, 4, 5]: break