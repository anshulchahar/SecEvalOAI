from django.http import HttpResponseRedirect
from django.urls import reverse

def http_responser_redirect(request):
    '''
    Get the target url from the request and redirect to it.
    '''
    # Assume the target URL is passed as a query parameter named 'next'
    target_url = request.GET.get('next')

    # If no target URL is provided, you might want to redirect to a default URL
    if not target_url:
        # Example: redirect to the home page or any other default page
        target_url = reverse('home')  # Assuming 'home' is the name of a URL pattern

    return HttpResponseRedirect(target_url)