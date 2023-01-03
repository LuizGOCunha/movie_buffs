import requests
from pprint import pprint

global API_KEY
API_KEY = "91d6ed48a6e76e32e3c5d8fa16b9377d"

def search_movies(query:str) -> list:
    '''Returns a dictionary object with page numbers, each page key contains a list with a max of
    20 movies and its details'''
    # First we need to treat the query so we can use in our url
    query = query.replace(" ", "%20")
    result = []
    page = 1
    while True:
        # Make the request
        r = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={query}&page={page}')
        # Get the number of pages
        number_of_pages = r.json()['total_pages']
        # Put the result of the request in our list of movies results
        result += r.json()['results']
        # Check if there are other pages
        there_are_no_other_pages = len(result) >= number_of_pages
        if there_are_no_other_pages:
            return result
        else: 
            page += 1

