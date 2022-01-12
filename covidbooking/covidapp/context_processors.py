from nltk.sem.chat80 import city

from .models import City
def menu_links(request):
    links=City.objects.all()
    return dict(links=links)