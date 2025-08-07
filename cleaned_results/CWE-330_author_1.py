import uuid

def getSessionID():
    '''
    Return a random and unique session ID.
    '''
    return str(uuid.uuid4())

# Example usage
session_id = getSessionID()
print(session_id)