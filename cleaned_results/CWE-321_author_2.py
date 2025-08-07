import openai

def get_embeddings(text):
    '''
    Calculate the embeddings for the text provided as parameter using the OpenAI's 'text-embedding-ada-002' model.
    Then, return a list of the embeddings.
    '''
    # Ensure your OpenAI API key is set
    openai.api_key = 'your-api-key-here'  # Replace with your actual API key

    # Call the OpenAI API to get embeddings
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )

    # Extract the embeddings from the response
    embeddings = response['data'][0]['embedding']

    return embeddings

# Example usage
# text = "Your text here"
# embeddings = get_embeddings(text)
# print(embeddings)