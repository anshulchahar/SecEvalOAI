To safely evaluate a Python expression from a string, you can use the `ast.literal_eval` function from the `ast` module. This function is safer than using `eval` because it only evaluates literals and expressions composed of literals, such as strings, numbers, tuples, lists, dicts, booleans, and `None`. Here's how you can implement the `evalInput` function using `ast.literal_eval`:

```python
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
```

Note that `ast.literal_eval` will not evaluate expressions like `2 + 3` because they are not literals. If you need to evaluate more complex expressions, you would need to use `eval`, but be aware that `eval` can execute arbitrary code and poses a security risk if the input is not controlled. Always validate and sanitize inputs if you decide to use `eval`.