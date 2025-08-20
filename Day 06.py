def find_zero_sum_subarrays(arr):
    prefix_sum = 0
    seen = {0: [-1]}  # prefix sum 0 at index -1 (to handle from start)
    result = []

    for i, num in enumerate(arr):
        prefix_sum += num
        
        # If prefix_sum seen before → zero-sum subarray(s) exist
        if prefix_sum in seen:
            for start in seen[prefix_sum]:
                result.append((start + 1, i))
        
        # Store current index for this prefix_sum
        if prefix_sum in seen:
            seen[prefix_sum].append(i)
        else:
            seen[prefix_sum] = [i]
    
    return result


# Example usage
arr = [1, 2, -3, 3, -1, 2]
print(find_zero_sum_subarrays(arr))
