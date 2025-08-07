To compute the n-th Fibonacci number using loops, you can use an iterative approach. Here's a Python function that does that:

```python
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
```

### Explanation:
- The function first checks if `n` is less than or equal to 0, returning 0 in that case, as the Fibonacci sequence is typically defined starting from the 0th or 1st position.
- If `n` is 1, it returns 1, as the first Fibonacci number is 1.
- For other values of `n`, it initializes two variables, `a` and `b`, to represent the first two Fibonacci numbers, 0 and 1, respectively.
- It then uses a loop to iterate from 2 to `n`, updating `a` and `b` to hold the last two Fibonacci numbers at each step.
- Finally, it returns `b`, which holds the n-th Fibonacci number after the loop completes.