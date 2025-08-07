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