import math

def binary_search_closest(arr, target):
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == target:
            return middle

        elif arr[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    # Compare the two candidates around the insertion position
    if left == 0:
        return 0

    if left == len(arr):
        return len(arr) - 1

    if abs(arr[left] - target) < abs(arr[left - 1] - target):
        return left

    return left - 1

    
    pass