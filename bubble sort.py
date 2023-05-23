def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
numbers = [5, 2, 8, 12, 1, 6, 4]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)
