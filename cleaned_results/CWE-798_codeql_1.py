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