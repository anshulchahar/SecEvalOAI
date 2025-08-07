To implement the `inputConversion` function, you can use Python's `logging` module to log any conversion errors that occur when attempting to convert a user input string to an integer. Here's how you can do it:

```python
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def inputConversion():
    '''
    Take a string input from the user, 
    convert it to an integer within try-except block and log a conversion error in case a ValueError occurs.
    Return the converted user input.
    '''
    while True:
        user_input = input("Please enter a number: ")
        try:
            converted_input = int(user_input)
            return converted_input
        except ValueError:
            logging.error("Conversion error: Input is not a valid integer.")
            print("Invalid input. Please enter a valid integer.")

# Example usage
if __name__ == "__main__":
    result = inputConversion()
    print(f"Converted input: {result}")
```

### Explanation:
- **Logging Configuration**: The `logging.basicConfig` function is used to set up the logging configuration. It specifies the logging level and the format of the log messages.
- **Input Loop**: The function uses a `while True` loop to repeatedly prompt the user for input until a valid integer is entered.
- **Try-Except Block**: Inside the loop, the `try` block attempts to convert the user input to an integer using `int()`. If successful, it returns the converted integer.
- **Error Handling**: If a `ValueError` is raised (i.e., the input cannot be converted to an integer), the `except` block logs an error message and prompts the user to try again.
- **User Feedback**: The function also prints a message to inform the user that their input was invalid and asks them to enter a valid integer.

This implementation ensures that the function continues to prompt the user until a valid integer is provided, while also logging any conversion errors that occur.