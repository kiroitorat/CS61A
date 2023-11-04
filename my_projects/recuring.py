def multiply(m, n):
    if n <=1:
        return m
    if n >1 :
        return multiply(m, n-1) + m

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2:
        return 2
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    from math import sqrt
    if n <=3:
        return True
    def helper(x):
        if x > sqrt(n):
            return True
        if n%x == 0:
            return False
        return helper(x+1)
    return helper(2)