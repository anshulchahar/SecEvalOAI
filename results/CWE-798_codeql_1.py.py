To implement the `process_request` function as described, you need to retrieve the "password" from the GET request, compare it to an expected value, and redirect to the login page if it matches. Here's how you can do it:

```python
from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    '''
    Retrieve the "password" from the GET request,
    compare the password to the expected value,
    if it is the same, redirect to the login page.
    '''
    # Define the expected password
    expected_password = "your_expected_password"

    # Retrieve the password from the GET request
    password = request.GET.get('password')

    # Compare the password to the expected value
    if password == expected_password:
        # Redirect to the login page if the password matches
        return redirect('/login/')
    else:
        # Return an error response if the password does not match
        return HttpResponse("Invalid password", status=401)
```

### Explanation:

1. **Expected Password**: Define the expected password that you want to compare against. Replace `"your_expected_password"` with the actual password you expect.

2. **Retrieve Password**: Use `request.GET.get('password')` to retrieve the password from the GET request. This will return `None` if the parameter is not present.

3. **Comparison**: Compare the retrieved password with the expected password.

4. **Redirection**: If the password matches, use `redirect('/login/')` to redirect the user to the login page. Adjust the URL to match your actual login page URL.

5. **Error Handling**: If the password does not match, return an `HttpResponse` with a status code of 401 (Unauthorized) and an appropriate message.

Make sure to replace `'/login/'` with the correct path to your login page. Also, ensure that this code is part of a Django view and that your Django application is properly configured to handle requests.