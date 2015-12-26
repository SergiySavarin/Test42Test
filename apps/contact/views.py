from django.shortcuts import render
from .models import Owner


def contact(request):
    """View for contact.html root page."""
    owner = Owner()
    # if owner have no data than create it
    if len(Owner.objects.all()) == 0:
        owner.first_name = 'Sergiy'
        owner.last_name = 'Savarin'
        owner.birthday = '30/11/1986'
        owner.email = 'vir.host@gmail.com'
        owner.skype = 'sergiy_savarin'
        owner.jabber = 'sergiysavarin@khavr.com'
        owner.other = 'www.facebook.com/sergiy.savarin'
        owner.bio = 'I was born in small town in Ukrainian Carpatians \
            in Lvivska region. There I finished school. Than I went to \
            study to Lviv Ivan Franko National University. In 2009 \
            I finished the university and stayed in Lviv making a lot \
            of diferent works. Life is awesome!!!'
        owner.save()
    owner = Owner.objects.all()[0]
    return render(request, 'contact.html', {'owner': owner})
