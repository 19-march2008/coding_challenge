import math

def lcm(N, M):
    return (N * M) // math.gcd(N, M)

# Example usage:
N = 4
M = 6
result = lcm(N, M)
print(result)  # Output: 12
