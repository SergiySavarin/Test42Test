from django.shortcuts import render
from .models import Owner, UsersRequest


def contact(request):
    """View for contact.html root page."""
    requests = UsersRequest.objects.order_by('id').reverse()[:10]
    owner = Owner.objects.all()[0]
    if request.is_ajax():
        return render(request, 'requests.html', {'requests': requests})
    else:
        return render(request, 'contact.html', {'owner': owner,
                                                'requests': requests})
