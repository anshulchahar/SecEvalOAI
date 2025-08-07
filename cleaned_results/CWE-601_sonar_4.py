from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect

def set_location_header(request):
    '''
    Get the "next" value from the request and redirect to it using the 'Location' header.
    '''
    # Try to get the 'next' parameter from GET or POST data
    next_url = request.GET.get('next') or request.POST.get('next')

    # If 'next' is not provided, you can set a default URL or handle it as needed
    if not next_url:
        # Optionally, you can redirect to a default URL or return an error
        return HttpResponse("No 'next' parameter provided.", status=400)

    # Redirect to the 'next' URL
    return HttpResponseRedirect(next_url)