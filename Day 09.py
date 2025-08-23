def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Start with the first string as the prefix
    prefix = strs[0]
    
    # Compare prefix with every string in the list
    for s in strs[1:]:
        # Reduce the prefix until it matches the start of the string s
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# Example usage
strs = ["flower", "flow", "flight"]
print("Longest Common Prefix:", longest_common_prefix(strs))
