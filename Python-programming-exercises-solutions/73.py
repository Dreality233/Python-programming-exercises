def bin_search(li,element):
    left = 0
    right = len(li)-1
    index = -1
    while left <= right:
        mid = left + (right-left)//2
        if li[mid] == element:
            return mid
        elif li[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    return index

li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12))