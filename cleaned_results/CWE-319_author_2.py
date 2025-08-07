import ftplib
import os

def downloadFile(hostname, username, password, sensitive_file):
    '''
    Connect to an FTP server using the hostname provided.
    Log-in using the username and password provided as parameters.
    Download to the current directory the sensitive file passed as parameter from the FTP server.
    '''
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(hostname)
        print(f"Connected to {hostname}")

        # Login to the server
        ftp.login(user=username, passwd=password)
        print(f"Logged in as {username}")

        # Open a local file to write the downloaded content
        with open(sensitive_file, 'wb') as local_file:
            # Define a callback function to write data to the local file
            def write_data(data):
                local_file.write(data)

            # Retrieve the file from the server
            ftp.retrbinary(f'RETR {sensitive_file}', write_data)
            print(f"Downloaded {sensitive_file} to the current directory")

        # Quit the FTP session
        ftp.quit()
        print("FTP session closed")

    except ftplib.all_errors as e:
        print(f"FTP error: {e}")

# Example usage:
# downloadFile('ftp.example.com', 'username', 'password', 'sensitive_file.txt')