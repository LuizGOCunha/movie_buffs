from django.shortcuts import render
from .forms import SearchBar
from django.core.handlers.wsgi import WSGIRequest
from .tmdb import search_movies

# Create your views here.

def search_bar(request:WSGIRequest):
    context = {}
    context['form'] = SearchBar
    print("This is the request:", type(request))
    print("resquest.get:", request.GET)
    if request.GET:
        search = context['search']
#        results = search_movies(search)

    return render(request, "search_bar.html", context)