import json

from django import forms
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Owner, UsersRequest


class EditContact(forms.Form):
    """Form for edit contact information page."""
    owner = Owner.objects.all().first()
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'value': owner.first_name, 'name': 'first_name',
        'id': 'first_name', 'class': 'form-control'
    }))
    last_name = forms.CharField(max_length=256)
    birthday = forms.DateField()
    email = forms.EmailField()
    skype = forms.CharField(max_length=256)
    jabber = forms.CharField(max_length=256)
    photo = forms.ImageField()
    # Other information about owner
    other = forms.CharField(widget=forms.Textarea)
    # Owner biography
    bio = forms.CharField(widget=forms.Textarea)


def contact(request):
    """View for contact.html root page."""
    # Take owner data from the database
    owner = Owner.objects.all()
    if not owner.first():
        return render(request, 'contact.html')
    return render(request, 'contact.html', {'owner': owner.first()})


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
    form = EditContact()
    owner = Owner.objects.all().first()
    if request.method == 'GET' and owner is not None:
        return render(request, 'edit_contact.html', {'owner': owner,
                                                     'form': form})
    elif request.method == 'POST':
        if request.is_ajax:
            return HttpResponseRedirect(reverse('edit_contact'))
        if request.POST.get('save_button') is not None:
            return HttpResponseRedirect(reverse('edit_contact'))
        elif request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(reverse('contact'))
