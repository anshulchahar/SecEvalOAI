import os

def createExecutableFile(data):
    # Define the filename
    filename = 'test.bim'
    
    # Write the binary data to the file
    with open(filename, 'wb') as file:
        file.write(data)
    
    # Change the file permissions to make it executable
    # 0o755 gives read, write, and execute permissions to the owner,
    # and read and execute permissions to group and others
    os.chmod(filename, 0o755)

# Example binary data
binary_data = b'\x7fELF...'  # Replace with actual binary content

# Create the executable file
createExecutableFile(binary_data)