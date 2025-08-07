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