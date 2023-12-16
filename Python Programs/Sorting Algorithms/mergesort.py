def mergesort(arr):
    if len(arr) <= 1:
        return
                      #  0   1  2   3  4  5   6   7 
    mid = len(arr)//2 # [10, 3, 15, 7, 8, 23, 98, 29]
    left = arr[:mid]
    right = arr[mid:]
    mergesort(left)
    mergesort(right)

    merge_sorted_list(left, right, arr)

def merge_sorted_list(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i] 
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1 

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1 

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1 


arr = [10, 3, 15, 7, 8, 23, 98, 29]
mergesort(arr)
print(arr)