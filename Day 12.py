def is_valid(s: str) -> bool:
    stack = []
    # Map closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map.values():  # If it's an opening bracket
            stack.append(char)
        elif char in bracket_map:  # If it's a closing bracket
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:
            # Invalid character found (not a bracket)
            return False

    return not stack  # If stack is empty, all brackets matched

# Example usage
s = "[{()}]"
print(is_valid(s))  # Output: True
