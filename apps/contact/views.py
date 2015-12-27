from django.shortcuts import render
from .models import Owner


def contact(request):
    """View for contact.html root page."""
    owner = Owner.objects.all()[0]
    return render(request, 'contact.html', {'owner': owner})
