# Primality tests: trial division, probability tests (e.g. Miller–Rabin), AKS
# Prime Sieves
# List of computer algebra systems: SageMath, SymPy
# Ref.: https://en.wikipedia.org/wiki/Primality_test

# Ref.: https://en.wikipedia.org/wiki/Primality_test#Python_Code
def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
