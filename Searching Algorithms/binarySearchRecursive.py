def binary_search_recursive(number_list, number_to_find, left, right):
    if left > right:
        return -1
    
    mid_index = (left + right)//2
    mid_number = number_list[mid_index]
    if mid_number == number_to_find:
        return mid_index
    
    if mid_number < number_to_find:
        left = mid_index + 1
    
    if mid_number > number_to_find:
        right = mid_index - 1

    return binary_search_recursive(number_list, number_to_find, left, right)


number_list = [12, 15, 17, 19, 21, 24, 45, 67]
number_to_find = 88

print(binary_search_recursive(number_list, number_to_find, 0, len(number_list)-1))
