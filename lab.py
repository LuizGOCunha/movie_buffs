import requests
from pprint import pprint

global API_KEY
API_KEY = "91d6ed48a6e76e32e3c5d8fa16b9377d"
#r = requests.get(url=f'https://api.themoviedb.org/3/movie/76341?api_key={API_KEY}')

r = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query=lkklsd&page=3')

#pprint(r.json())
#print(len(r.json()['results']))

def search_movies(query:str):
    # First we need to treat the query so we can use in our url
    query = query.replace(" ", "%20")
    result = {}
    page = 1
    while True:
        # Make the request
        r = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={query}&page={page}')
        # Get the number of pages
        number_of_pages = r.json()['total_pages']
        # Put the result of the request in our result dictionary with its appropriate page number
        result[f'Page {page}'] = r.json()['results']
        # Check if there are other pages
        there_are_no_other_pages = len(result) >= number_of_pages
        if there_are_no_other_pages:
            return result
        else: 
            page += 1
    
query_results = search_movies("Indiana Jones")

        