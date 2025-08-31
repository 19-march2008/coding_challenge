def prime_factors(N):
    factors = []
    # Divide out all 2s
    while N % 2 == 0:
        factors.append(2)
        N //= 2
    
    # Try odd numbers from 3 up to sqrt(N)
    i = 3
    while i * i <= N:
        while N % i == 0:
            factors.append(i)
            N //= i
        i += 2

    # If N is still greater than 1, it is prime
    if N > 1:
        factors.append(N)

    return factors

# Example usage
N = 18
print(prime_factors(N))  # Output: [2, 3, 3]
