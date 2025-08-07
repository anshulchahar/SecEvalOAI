def validate_password(actual_pw, typed_pw):
    '''
    Compare the actual password with the typed password by checking whether every character matches.
    
    Parameters:
    actual_pw (str): The actual password.
    typed_pw (str): The password entered by the user.
    
    Returns:
    bool: True if the passwords match exactly, False otherwise.
    '''
    return actual_pw == typed_pw