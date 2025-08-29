def length_of_longest_substring(s: str) -> int:
    char_index = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1  # Move left pointer to the right of last occurrence

        char_index[s[right]] = right  # Update last seen index of current character
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage
S = "abcabcbb"
print(length_of_longest_substring(S))  # Output: 3
