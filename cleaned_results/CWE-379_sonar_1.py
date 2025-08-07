import tempfile

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    '''
    # Create a NamedTemporaryFile with delete=False so it persists after closing
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as temp_file:
        # Write the results to the file
        temp_file.write(results)
        # Return the path of the temporary file
        return temp_file.name