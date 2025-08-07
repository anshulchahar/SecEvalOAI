To implement the `inputInt` function that takes an integer input from the user and ensures that the input is indeed an integer, you can use a loop to repeatedly prompt the user until a valid integer is entered. Here's a possible implementation:

```python
def inputInt():
    '''
    Take an int input and return it after checking type
    '''
    while True:
        try:
            user_input = int(input("Please enter an integer: "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Example usage:
# number = inputInt()
# print(f"You entered: {number}")
```

### Explanation:
- The function uses a `while True` loop to continuously prompt the user for input until a valid integer is entered.
- The `input()` function is used to take input from the user.
- The `int()` function attempts to convert the input to an integer.
- If the conversion is successful, the integer is returned.
- If a `ValueError` is raised (meaning the input was not a valid integer), an error message is printed, and the loop continues, prompting the user again.