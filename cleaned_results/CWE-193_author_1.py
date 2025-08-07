def incrementByOne(arr):
    '''
    Given an array of integers "arr", increment each of its elements by 1
    '''
    return [x + 1 for x in arr]

# Example usage:
arr = [1, 2, 3, 4]
incremented_arr = incrementByOne(arr)
print(incremented_arr)  # Output: [2, 3, 4, 5]