import json

from forms import EditContactForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from resizeimg import size, resize

from fortytwo_test_task.settings import MEDIA_ROOT
from .models import Owner, UsersRequest


def contact(request):
    """View for contact.html root page."""
    # Take owner data from the database
    owner = Owner.objects.first()
    return render(request, 'contact.html', {'owner': owner})


def requests(request):
    """View for last ten requests to server."""
    # Take last ten requests from the database and sort its by id
    requests = UsersRequest.objects.order_by('id').reverse()[:10]
    # Quantity of requests
    count = UsersRequest.objects.count()
    # if request is ajax, prepare requests and
    # send its in json format
    if request.is_ajax():
        response_data = {
            'request': [('<p>%s</p>' % user.request_str) for user in requests],
            'count': count
        }
        return HttpResponse(json.dumps(response_data))
    else:
        return render(request, 'requests.html', {'requests': requests})


@login_required
def edit_contact(request):
    """View for editing owner data."""
    form = EditContactForm()
    owner = Owner.objects.first()
    if request.method == 'GET':
        form = EditContactForm(instance=owner)
        return render(request, 'edit_contact.html', {'form': form})
    elif request.method == 'POST':
        if request.POST.get('save_button') is not None:
            form = EditContactForm(request.POST, request.FILES, instance=owner)
            if form.is_valid():
                owner = form.save()
                owner.save()
                # Take owner photo path
                photo_path = '%s/%s' % (MEDIA_ROOT, owner.photo)
                # Check photo size, if not 200x200px, resize it
                if not size(photo_path):
                    resize(photo_path)
            else:
                if request.is_ajax():
                    errors = {}
                    for error in form.errors:
                        errors[error] = form.errors[error]
                        print form.errors[error]
                    return HttpResponseBadRequest(json.dumps(errors))
            return HttpResponseRedirect(reverse('edit_contact'))
        else:
            form = EditContactForm(request.POST)
            return render(request, 'edit_contact.html', {'form': form})
