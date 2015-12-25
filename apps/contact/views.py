from django.shortcuts import render

def contact(request):
    """View for contact.html root page."""
    return render(request, 'contact.html')