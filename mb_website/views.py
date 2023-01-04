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
    if 'search' in request.GET.keys():
        # Get the search from the parameters
        search = request.GET['search']
        print("*****", search)
        # Search through the API
        results = search_movies(search)
        models = []
        for movie in results:
            model = Movie(title=movie["title"], overview=movie["overview"], release_date=movie["release_date"], rating=movie['vote_average'])
            models.append(model)

        # Create Paginator instance
        paginator = Paginator(models, 3)
        # Get the page number that is being requested
        page_number = request.GET.get('page', 1)
        # Exhibit the appropriate page number
        page = paginator.page(page_number)
        # Pass the page content in the context instead of the raw info
        context['movies'] = page
        
    return render(request, "search_bar.html", context)