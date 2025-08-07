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