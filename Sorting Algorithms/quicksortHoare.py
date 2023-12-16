def swap(start, end, arr):
    if start != end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp

def partition(element, start, end):
    pivot_index = start
    pivot = element[pivot_index]

    while start < end:
        while start < len(element) and element[start] <= pivot:
            start += 1

        while element[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, element)

    swap(pivot_index, end, element)

    return end

def quicksort(element, start, end):
    if start < end:
        pivot_pos = partition(element, start, end)
        quicksort(element, start, pivot_pos - 1)
        quicksort(element, pivot_pos + 1, end)
    


arr = [11, 9, 29, 7, 2, 15, 28]
quicksort(arr, 0, len(arr)-1)

print(arr)
