To download a file from an FTP server using Python, you can use the `ftplib` module, which provides a simple interface to interact with FTP servers. Below is a sample implementation of the `downloadFile` function that connects to an FTP server, logs in with the provided credentials, and downloads a specified file:

```python
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
```

### Key Points:
- **Connection**: The `ftplib.FTP` object is used to establish a connection to the FTP server.
- **Login**: The `login` method is used to authenticate with the server using the provided username and password.
- **File Download**: The `retrbinary` method is used to download the file in binary mode. The `write_data` function is a callback that writes the downloaded data to a local file.
- **Error Handling**: The `try-except` block is used to catch and print any FTP-related errors.
- **Resource Management**: The `with` statement ensures that the local file is properly closed after the download is complete.

Make sure to replace `'ftp.example.com'`, `'username'`, `'password'`, and `'sensitive_file.txt'` with