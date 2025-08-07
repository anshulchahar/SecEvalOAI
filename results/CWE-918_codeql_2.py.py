To complete the `retrieve_info` function, you'll need to extract the `user_id` from the request, make a request to the GitHub API to get the user information, and then return that information as a response. Here's how you can implement this:

```python
@app.route("/user")
def retrieve_info():
    '''
    Get the user_id from the request,
    then retrieve the user info from GitHub using the GitHub's API,
    and return the response
    '''
    # Get the user_id from the query parameters
    user_id = request.args.get('user_id')
    
    if not user_id:
        return {"error": "user_id parameter is required"}, 400

    # GitHub API URL for user information
    github_api_url = f"https://api.github.com/users/{user_id}"

    try:
        # Make a GET request to the GitHub API
        response = requests.get(github_api_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Return the JSON response from GitHub
            return response.json()
        else:
            # Return an error message if the user is not found or another error occurred
            return {"error": "User not found or an error occurred"}, response.status_code
    except requests.RequestException as e:
        # Handle any exceptions that occur during the request
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(debug=True)
```

### Explanation:

1. **Extracting `user_id`:** The `user_id` is extracted from the query parameters using `request.args.get('user_id')`.

2. **GitHub API Request:** A request is made to the GitHub API using the `requests` library to fetch user information.

3. **Error Handling:** 
   - If `user_id` is not provided, a 400 error is returned.
   - If the GitHub API request fails or the user is not found, an appropriate error message and status code are returned.
   - If an exception occurs during the request, a 500 error with the exception message is returned.

4. **Running the Flask App:** The app is set to run in debug mode for easier troubleshooting during development.