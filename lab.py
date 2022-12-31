import requests
from pprint import pprint

global API_KEY
API_KEY = "91d6ed48a6e76e32e3c5d8fa16b9377d"
#r = requests.get(url=f'https://api.themoviedb.org/3/movie/76341?api_key={API_KEY}')

r = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query=lkklsd&page=3')

#pprint(r.json())
#print(len(r.json()['results']))

        