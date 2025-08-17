def findDuplicate(arr):
    # Phase 1: Finding the intersection point of two runners.
    slow = arr[0]
    fast = arr[0]
    
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    
    # Phase 2: Find the entrance to the cycle.
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return slow

# Example
arr = [3, 1, 3, 4, 2]
print("Duplicate number:", findDuplicate(arr))
