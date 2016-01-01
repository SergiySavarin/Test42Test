import json

from django.http import HttpResponse
from django.shortcuts import render
from .models import Owner, UsersRequest


def contact(request):
    """View for contact.html root page."""
    # Take last ten requests from the database and sort its by id
    requests = UsersRequest.objects.order_by('id').reverse()[:10]
    # Take owner data from the database
    owner = Owner.objects.all()[0]
    # if request is ajax, prepare requests and
    # send its in json format
    if request.is_ajax():
        request_data = {
            'request': [('<p>%s</p>' % user.request_str) for user in requests]
        }
        return HttpResponse(json.dumps(request_data))
    else:
        return render(request, 'contact.html', {'owner': owner,
                                                'requests': requests})
