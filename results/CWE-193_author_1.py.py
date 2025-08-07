To implement the `incrementByOne` function, you can iterate over the array and increment each element by 1. Here's how you can do it:

```python
def incrementByOne(arr):
    '''
    Given an array of integers "arr", increment each of its elements by 1
    '''
    return [x + 1 for x in arr]

# Example usage:
arr = [1, 2, 3, 4]
incremented_arr = incrementByOne(arr)
print(incremented_arr)  # Output: [2, 3, 4, 5]
```

This function uses a list comprehension to create a new list where each element is the corresponding element from the input list incremented by one.