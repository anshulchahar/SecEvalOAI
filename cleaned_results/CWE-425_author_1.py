import os
from django.http import HttpResponse, Http404
from django.conf import settings

def getResource(request):
    '''
    Get username and date from the request, then
    send the file to the user by creating path by the username and date.
    '''
    # Extract username and date from the request
    username = request.GET.get('username')
    date = request.GET.get('date')

    # Validate the inputs
    if not username or not date:
        return HttpResponse("Username and date are required.", status=400)

    # Construct the file path
    file_path = os.path.join(settings.MEDIA_ROOT, username, f"{date}.txt")

    # Check if the file exists
    if not os.path.exists(file_path):
        raise Http404("File not found.")

    # Open the file and send it as a response
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        return response