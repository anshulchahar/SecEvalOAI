def convert_to_int():
    '''
    Take an input from the user (console) and convert it to int within a try-except block.
    '''
    user_input = input("Please enter a number: ")
    try:
        converted_number = int(user_input)
        print(f"The converted integer is: {converted_number}")
        return converted_number
    except ValueError:
        print("The input is not a valid integer.")
        return None

# Example usage
convert_to_int()