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