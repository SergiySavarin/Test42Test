from django.shortcuts import render

def contact(request):
    owner = {
        'name': 'Sergiy',
        'last_name': 'Savarin',
        'birth_date': '30/11/1986',
        'email': 'vir.host@gmail.com',
        'jabber': 'sergiysavarin@khavr.com',
        'skype': 'sergiy_savarin',
        'facebook': 'www.facebook.com/sergiy.savarin',
        'bio': 'I was born in small town in Ukrainian Carpatians in \
                Lvivska region. There I finished school. Than I went \
                to study to Lviv Ivan Franko National University. In \
                2009 I finished the university and stayed in Lviv making \
                a lot of diferent works. Life is awesome!!!'
    }
    return render(request, 'contact.html', {'owner': owner})