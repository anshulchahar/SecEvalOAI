To calculate embeddings using OpenAI's `text-embedding-ada-002` model, you'll need to use the OpenAI API. Here's a step-by-step guide on how to implement the `get_embeddings` function:

1. **Install the OpenAI Python Package**: Make sure you have the OpenAI Python package installed. You can install it using pip if you haven't already:

   ```bash
   pip install openai
   ```

2. **Set Up Your API Key**: Ensure you have your OpenAI API key ready. You can set it as an environment variable or directly in your script (though the former is more secure).

3. **Implement the Function**: Use the OpenAI API to get the embeddings for the given text. Here's how you can implement the `get_embeddings` function:

```python
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
```

**Notes**:
- Replace `'your-api-key-here'` with your actual OpenAI API key.
- The function sends a request to the OpenAI API to compute the embeddings for the input text using the specified model.
- The response contains the embeddings, which are extracted and returned as a list.

**Security Considerations**:
- Avoid hardcoding your API key directly in the script. Instead, consider using environment variables or a configuration file to manage sensitive information securely.
- Be mindful of the API usage and costs associated with using OpenAI's services.