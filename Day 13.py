def longest_palindrome(s: str) -> str:
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the palindromic substring
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Odd length palindrome
        palindrome1 = expand_around_center(i, i)
        # Even length palindrome
        palindrome2 = expand_around_center(i, i + 1)
        # Choose the longer one
        if len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest

# Example usage:
print(longest_palindrome("babad"))  # Output: "bab" (or "aba")
