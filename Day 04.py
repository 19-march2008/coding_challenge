import math

def merge_in_place(arr1, arr2):
    m, n = len(arr1), len(arr2)

    def next_gap(gap):
        if gap <= 1:
            return 0
        return math.ceil(gap / 2)

    gap = next_gap(m + n)

    while gap > 0:
        # Compare and swap elements in arr1
        i = 0
        while i + gap < m:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1

        # Compare and swap between arr1 and arr2
        j = gap - m if gap > m else 0
        while i < m and j < n:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        # Compare and swap elements in arr2
        j = 0
        while j + gap < n:
            if arr2[j] > arr2[j + gap]:
                arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
            j += 1

        gap = next_gap(gap)

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

merge_in_place(arr1, arr2)

print("arr1:", arr1)  # Output: [1, 2, 3, 4]
print("arr2:", arr2)  # Output: [5, 6, 7, 8]

