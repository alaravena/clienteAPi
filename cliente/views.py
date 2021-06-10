from django.shortcuts import render
from .services import get_starWars

# Create your views here.
def home(request):
    data = {
        'listado': get_starWars()
    }
    return render(request, 'cliente/home.html',data)