To generate a random and unique session ID, you can use Python's `uuid` module, which is specifically designed for generating universally unique identifiers. Here's how you can implement the `getSessionID` function using `uuid`:

```python
import uuid

def getSessionID():
    '''
    Return a random and unique session ID.
    '''
    return str(uuid.uuid4())

# Example usage
session_id = getSessionID()
print(session_id)
```

This function uses `uuid.uuid4()`, which generates a random UUID. The `uuid4` method creates a UUID based on random numbers, ensuring that the generated session ID is both random and unique. The `str()` function is used to convert the UUID object to a string, which is typically the desired format for session IDs.