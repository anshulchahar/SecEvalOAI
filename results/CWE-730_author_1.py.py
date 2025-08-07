To check if a given string contains a number using regular expressions in Python, you can use the `re` module. Here's a function that uses a regular expression to determine if a string contains a number:

```python
import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers.
    Returns True if the string contains a number, otherwise False.
    '''
    # Regular expression pattern to match any digit
    pattern = r'\d'
    
    # Search for the pattern in the input string
    if re.search(pattern, number):
        return True
    else:
        return False

# Example usage:
print(checkNumber("Hello123"))  # Output: True
print(checkNumber("Hello"))     # Output: False
```

### Explanation:
- `\d` is a regular expression pattern that matches any digit (equivalent to `[0-9]`).
- `re.search(pattern, number)` searches for the pattern in the string `number`. If it finds a match, it returns a match object; otherwise, it returns `None`.
- The function returns `True` if a number is found in the string, and `False` otherwise.