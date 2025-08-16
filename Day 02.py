
def find_missing_number(arr):
    n = len(arr) + 1  # since one number is missing
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example
arr = [1, 2, 4, 5]
print("Missing number:", find_missing_number(arr))
