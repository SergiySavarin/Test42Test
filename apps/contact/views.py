from django.http import HttpResponse
from django.shortcuts import render
from .models import Owner, UsersRequest
import json

def contact(request):
    """View for contact.html root page."""
    requests = UsersRequest.objects.order_by('id').reverse()[:10]
    owner = Owner.objects.all()[0]
    if request.is_ajax():
        request_data = {'request': [user.request_str for user in requests]}
        return HttpResponse(json.dumps(request_data), content_type='application/javascript')
    else:
        return render(request, 'contact.html', {'owner': owner,
                                            'requests': requests})

def requests(request):
    """for requests storing"""
    requests = UsersRequest.objects.order_by('id').reverse()[:10]
    request_data = {'request': [user.request_str for user in requests]}
    # return HttpResponse(json.dumps(request_data), content_type='application/javascript')
    return render(request, 'requests.html', {'requests': requests})
