def shellsort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j>=gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor

        gap = gap // 2


arr = [11, 9, 29, 7, 2, 15, 28]
shellsort(arr)
print(arr)