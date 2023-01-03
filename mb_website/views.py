from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator

from .tmdb import search_movies
from .forms import SearchBar
from .models import Movie

# Create your views here.

def search_bar(request:WSGIRequest):
    context = {}
    context['form'] = SearchBar
    object_list = list(range(10))
    print("This is the request:", type(request))
    print("resquest.get:", request.GET)
    if 'search' in request.GET.keys():
        # Get the search from the parameters
        search = request.GET['search']
        # Search through the API
        results = search_movies(search)
        models = []
        for movie in results:
            model = Movie(title=movie["title"], overview=movie["overview"], release_date=movie["release_date"], rating=movie['vote_average'])
            models.append(model)

        context['movies'] = models
        
    return render(request, "search_bar.html", context)