To implement the `getResource` function, you'll need to extract the `username` and `date` from the request, construct the file path, and then serve the file to the user. Here's a basic implementation:

```python
import os
from django.http import HttpResponse, Http404
from django.conf import settings

def getResource(request):
    '''
    Get username and date from the request, then
    send the file to the user by creating path by the username and date.
    '''
    # Extract username and date from the request
    username = request.GET.get('username')
    date = request.GET.get('date')

    # Validate the inputs
    if not username or not date:
        return HttpResponse("Username and date are required.", status=400)

    # Construct the file path
    file_path = os.path.join(settings.MEDIA_ROOT, username, f"{date}.txt")

    # Check if the file exists
    if not os.path.exists(file_path):
        raise Http404("File not found.")

    # Open the file and send it as a response
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        return response
```

### Key Points:

1. **Extract Parameters**: The `username` and `date` are extracted from the query parameters of the request. You might need to adjust this if the parameters are sent differently (e.g., via POST data).

2. **File Path Construction**: The file path is constructed using `os.path.join` to ensure proper path formatting. The example assumes the files are stored in a directory structure under `MEDIA_ROOT`.

3. **File Existence Check**: Before attempting to open the file, the code checks if the file exists to avoid errors.

4. **File Serving**: The file is opened in binary mode and served with a content type of `application/octet-stream`, which is suitable for arbitrary binary data. The `Content-Disposition` header is set to prompt a download with the original filename.

5. **Error Handling**: If the username or date is missing, or if the file does not exist, appropriate error responses are returned.

Make sure to adjust the file extension and path logic according to your actual use case. Also, ensure that your application has the necessary permissions to read the files from the specified directory.