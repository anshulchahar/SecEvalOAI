def getFibonacci(n):
    '''
    Compute the n-th Fibonacci number using loops only.
    '''
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage:
# print(getFibonacci(10))  # Output: 55