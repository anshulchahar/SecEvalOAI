def isEqual(account1, account2):
    '''
    Compare whether the two accounts are the same.
    
    Parameters:
    account1 (dict): The first account to compare.
    account2 (dict): The second account to compare.
    
    Returns:
    bool: True if the accounts are the same, False otherwise.
    '''
    # Define the keys that should be compared to determine if accounts are equal
    keys_to_compare = ['account_number', 'name', 'email']
    
    for key in keys_to_compare:
        if account1.get(key) != account2.get(key):
            return False
    
    return True

# Example usage:
account1 = {'account_number': '12345', 'name': 'John Doe', 'email': 'john@example.com'}
account2 = {'account_number': '12345', 'name': 'John Doe', 'email': 'john@example.com'}
account3 = {'account_number': '67890', 'name': 'Jane Doe', 'email': 'jane@example.com'}

print(isEqual(account1, account2))  # Output: True
print(isEqual(account1, account3))  # Output: False