To complete the `getRecord` function, you need to extract the data from the `request`, parse it using the `parse` function, and then return the length of the parsed data. Here's how you can implement this:

```python
def getRecord(request):
    '''
    Get the data from the request,
    parse it by invoking the parse() method,
    and return the length of the parsed data.
    '''
    # Assuming 'request' is a dictionary and 'data' is a key in that dictionary
    data = request.get('data', None)
    
    # Parse the data using the parse function
    parsed_data = parse(data)
    
    # Return the length of the parsed data
    # If parsed_data is None, return 0
    return len(parsed_data) if parsed_data is not None else 0
```

### Explanation:
- The function assumes that `request` is a dictionary-like object and attempts to retrieve the value associated with the key `'data'`.
- It uses the `parse` function to split the data string into a list.
- It checks if `parsed_data` is `None` (which would happen if `data` was `None`), and returns `0` in that case. Otherwise, it returns the length of the list obtained from parsing the data.