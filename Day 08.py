def reverseWords(s: str) -> str:
    # Step 1: Split string into words, automatically removes extra spaces
    words = s.split()
    
    # Step 2: Reverse the list of words
    reversed_words = words[::-1]
    
    # Step 3: Join them with single space
    return ' '.join(reversed_words)
