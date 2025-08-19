def find_leaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[-1]  # The rightmost element is always a leader
    leaders.append(max_from_right)

    # Traverse the array from second last to the beginning
    for i in range(n - 2, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]

    # Reverse to maintain the original order
    leaders.reverse()
    return leaders

# Example usage
arr = [16, 17, 4, 3, 5, 2]
print("Leaders:", find_leaders(arr))
