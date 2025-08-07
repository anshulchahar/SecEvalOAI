To generate a random string consisting of ASCII letters with a specified length, you can use the `random` module in Python. Here's a function that accomplishes this:

```python
import random
import string

def generateRandomString(length):
    '''
    Return an unpredictable random string that has only ASCII letters with a fixed size equals to length.
    '''
    # Use string.ascii_letters to get a string of all ASCII letters (both lowercase and uppercase)
    letters = string.ascii_letters
    # Use random.choices to select 'length' number of characters from 'letters'
    random_string = ''.join(random.choices(letters, k=length))
    return random_string

# Example usage:
random_string = generateRandomString(10)
print(random_string)
```

This function uses `string.ascii_letters` to get a string containing all ASCII letters (both lowercase and uppercase). The `random.choices` function is then used to randomly select `length` characters from this pool of letters, and `''.join()` is used to concatenate these characters into a single string.