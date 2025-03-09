def binarysearch_recursive(arr, left, right, target):
    if left > right:
        return -1  # Base case: target not found
    
    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binarysearch_recursive(arr, mid + 1, right, target)
    else:
        return binarysearch_recursive(arr, left, mid - 1, target)

# Example usage
arr = [1, 3, 5, 7, 9, 11]
target = 5
result = binarysearch_recursive(arr, 0, len(arr) - 1, target)
print("Target found at index:", result)
