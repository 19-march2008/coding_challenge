from collections import defaultdict

def count_substrings_with_at_most_k_distinct(s, k):
    n = len(s)
    left = 0
    freq = defaultdict(int)
    count = 0

    for right in range(n):
        freq[s[right]] += 1

        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        count += right - left + 1

    return count

def substrings_with_exactly_k_distinct(s, k):
    return (count_substrings_with_at_most_k_distinct(s, k) -
            count_substrings_with_at_most_k_distinct(s, k - 1))

# Example
s = "pqpqs"
k = 2
print(substrings_with_exactly_k_distinct(s, k))  # Output: 7
