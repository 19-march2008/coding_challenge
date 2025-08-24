from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    
    for word in strs:
        # Sort the word and use it as the key
        key = tuple(sorted(word))
        anagrams[key].append(word)
    
    # Return the grouped anagrams as a list of lists
    return list(anagrams.values())

# Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = groupAnagrams(strs)
print(result)
