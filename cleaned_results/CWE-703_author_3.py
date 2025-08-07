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