def permute_unique(s):
    def backtrack(path, counter):
        if len(path) == len(s):
            result.append("".join(path))
            return
        for char in counter:
            if counter[char] > 0:
                # Choose
                path.append(char)
                counter[char] -= 1
                # Explore
                backtrack(path, counter)
                # Un-choose
                path.pop()
                counter[char] += 1

    from collections import Counter
    result = []
    counter = Counter(s)
    backtrack([], counter)
    return result
print(permute_unique("abc"))

