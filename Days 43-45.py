#Search API and Consuming HTTP Services
from typing import List

import requests
import collections
import api

Movie = collections.namedtuple('Movie', 'imdb_code, title, director, keywords, '
                                        'duration, genres, rating, year, imdb_score')


def find_movie_by_title(keyword: str) -> List[Movie]:
    url = f'http://movie_service.talkpython.fm/api/search/{keyword}'

    resp = requests.get(url)
    resp.raise_for_status()

    results = resp.json()
    movies = []
    for r in results.get('hits'):
        movies.append(Movie(**r))

    return movies

def main():
    keyword = input('Keyword of title search: ')
    results = api.find_movie_by_title(keyword)

    print(f'There are {len(results)} movies found.')
    for r in results:
        print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")


if __name__ == '__main__':
    main()