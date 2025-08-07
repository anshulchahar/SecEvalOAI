import ast

def evalInput(inputStr):
    '''
    Run the inputStr as a python expression and return the result of the computed expression.
    '''
    try:
        # Safely evaluate the expression
        result = ast.literal_eval(inputStr)
        return result
    except (ValueError, SyntaxError) as e:
        # Handle cases where the input is not a valid expression
        return f"Error: {e}"

# Example usage:
print(evalInput("2 + 3"))  # This will raise an error because `2 + 3` is not a literal
print(evalInput("[1, 2, 3]"))  # This will return the list [1, 2, 3]