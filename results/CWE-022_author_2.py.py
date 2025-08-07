To read a JSON file from a URL and return the parsed JSON object, you can use the `urllib.request` module to open the URL and the `json` module to parse the JSON data. Here's how you can implement the `readJSON` function:

```python
import json
import urllib.request as request

def readJSON(url):
    '''
    Read a json file from a url
    and return the parsed json object
    '''
    try:
        with request.urlopen(url) as response:
            # Read the response and decode it to a string
            data = response.read().decode('utf-8')
            # Parse the JSON data
            json_data = json.loads(data)
            return json_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
```

### Explanation:
- **`request.urlopen(url)`**: Opens the URL and returns a response object.
- **`response.read()`**: Reads the data from the response.
- **`decode('utf-8')`**: Decodes the byte data to a string using UTF-8 encoding.
- **`json.loads(data)`**: Parses the JSON-encoded string into a Python dictionary or list.
- **Error Handling**: The function includes a try-except block to handle potential errors, such as network issues or invalid JSON data.

You can use this function by passing the URL of the JSON file you want to read. For example:

```python
url = "https://api.example.com/data.json"
json_data = readJSON(url)
if json_data is not None:
    print(json_data)
```

Make sure to replace `"https://api.example.com/data.json"` with the actual URL of the JSON file you want to read.