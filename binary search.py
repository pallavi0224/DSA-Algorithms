def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Start and end pointers

    while left <= right:
        mid = (left + right) // 2  # Find the middle index

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Target not found

# Example Usage
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
index = binary_search(arr, target)

print(f"Element found at index: {index}" if index != -1 else "Element not found")
