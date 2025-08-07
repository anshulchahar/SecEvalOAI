import os

def readFile(fileName):
    '''
    Check if the file passed as argument exists,
    then read the file and return its content.
    '''
    # Check if the file exists
    if not os.path.isfile(fileName):
        return "File does not exist."

    # Read the file and return its content
    try:
        with open(fileName, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"An error occurred while reading the file: {e}"

# Example usage:
# content = readFile('example.txt')
# print(content)