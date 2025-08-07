import pickle

def getPickleData(pickled):
    '''
    Return deserialized data from a trusted pickled source.
    '''
    try:
        # Deserialize the pickled data
        data = pickle.loads(pickled)
        return data
    except pickle.UnpicklingError as e:
        # Handle unpickling errors
        print("Error unpickling data:", e)
        return None
    except Exception as e:
        # Handle other exceptions
        print("An error occurred:", e)
        return None