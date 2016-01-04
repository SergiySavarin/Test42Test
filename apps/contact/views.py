import json

from django.http import HttpResponse
from django.shortcuts import render
from .models import Owner, UsersRequest


def contact(request):
    """View for contact.html root page."""
    # Take owner data from the database
    owner = Owner.objects.all().first()
    if owner is not None:
        return render(request, 'contact.html', {'owner': owner})
    return render(request, 'contact.html')


def requests(request):
    """View for last ten requests to server."""
    # Take last ten requests from the database and sort its by id
    requests = UsersRequest.objects.order_by('id').reverse()[:10]
    # Quantity of requests
    count = UsersRequest.objects.count()
    # if request is ajax, prepare requests and
    # send its in json format
    if request.is_ajax():
        request_data = {
            'request': [('<p>%s</p>' % user.request_str) for user in requests],
            'count': count
        }
        return HttpResponse(json.dumps(request_data))
    else:
        return render(request, 'requests.html')


def edit_contact(request):
    return render(request, 'edit_contact.html')
