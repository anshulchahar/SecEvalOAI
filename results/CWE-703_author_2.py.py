To continuously take input from the user and convert it to an integer using a try-except block, you can implement a loop that repeatedly prompts the user for input. If the input can be successfully converted to an integer, you can print or return the integer. If the conversion fails (i.e., the input is not a valid integer), you can catch the exception and prompt the user again. Here's how you can implement this:

```python
def convert_to_int():
    '''
    Continuously take an input from user and convert it to int within a try-except block
    '''
    while True:
        user_input = input("Enter an integer: ")
        try:
            # Try to convert the input to an integer
            number = int(user_input)
            print(f"Successfully converted to integer: {number}")
            # Optionally, break the loop if you only want one successful conversion
            break
        except ValueError:
            # Handle the case where the input is not a valid integer
            print("Invalid input. Please enter a valid integer.")

# Call the function to test it
convert_to_int()
```

In this implementation:
- The `while True` loop ensures that the program will keep asking for input until a valid integer is entered.
- The `try` block attempts to convert the input to an integer.
- If the conversion is successful, it prints the integer and breaks out of the loop.
- If a `ValueError` is raised (meaning the input was not a valid integer), the `except` block catches the exception and informs the user, then the loop continues.