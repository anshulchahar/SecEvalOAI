import boto3
from botocore.exceptions import ClientError

DYNAMO_CLIENT = boto3.client('dynamodb', config=config)

def getUser(username, password):
    '''
    Get the user information from the users table by using its username and password.
    '''
    try:
        # Query the DynamoDB table
        response = DYNAMO_CLIENT.get_item(
            TableName='users',
            Key={
                'username': {'S': username},
                'password': {'S': password}  # Note: This is not secure for real applications
            }
        )

        # Check if the item exists in the response
        if 'Item' in response:
            return response['Item']
        else:
            return None

    except ClientError as e:
        print(f"An error occurred: {e.response['Error']['Message']}")
        return None

# Example usage
user_info = getUser('example_username', 'example_password')
if user_info:
    print("User found:", user_info)
else:
    print("User not found or incorrect credentials.")