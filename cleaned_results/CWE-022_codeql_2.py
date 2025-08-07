import tarfile
import os

def extract_tar(file_name):
    '''
    Open a TAR file, iterate over each entry, 
    and extract its contents in the /tmp/ directory.
    '''
    # Ensure the /tmp/ directory exists
    extract_path = '/tmp/'
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)

    # Open the tar file
    with tarfile.open(file_name, 'r') as tar:
        # Iterate over each member in the tar file
        for member in tar.getmembers():
            # Extract each member to the /tmp/ directory
            tar.extract(member, path=extract_path)
            print(f'Extracted {member.name} to {extract_path}')

# Example usage:
# extract_tar('example.tar')