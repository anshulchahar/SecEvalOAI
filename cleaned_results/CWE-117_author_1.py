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