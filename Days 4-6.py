from collections import  defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve

# name tuple

user = ('bob', 'coder')

f'{user[0]} is a {user[1]}'
User = namedtuple('User', 'name role')
user = User(name='bob', role='coder')
# user.name
user.role
f'{user.name} is a {user.role}'


# defaultdict

users = {'bob': 'coder'}
users['bob']
users['julian']

users.get('bob')
users.get('julian')

challenge_done= [('mike', 10), ('julian', 7), ('bob', 5), ('mike', 11), ('julian', 8), ('bob', 6)]

challenges = {}
for name, challenge in challenges_done:
    challenges[name].append(challenge)


challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenges)
challenges

# Counter
words = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum""".split()
words[:5]

Counter(words).most_common(5)
# [('the', 6), ('Lorem', 4), ('Ipsum', 4), ('of', 4), ('and', 3)]

# Deque

lst = list(range(10000000))
deq = deque(range(10000000))

def insert_and_delete(ds):
    for_in range(10):
    index = random.choice(range(100))
    ds.remove(index)
    ds.insert(index, index)



timeit insert_and_delete(lst)
# 447 ms ± 45.7 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
timeit insert_and_delete(deq)
# 83.7 µs ± 13.7 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)



# Practice using movie data

movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'
urlretrieve(movie_data, movies_csv)

Movie = namedtuple('Movie', 'title year score')
def get_movies_by_director(data=movies_csv):
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors

directors = get_movies_by_director()

cnt = Counter()
for director, movies in directors.items():
    cnt[director] += len(movies)

cnt.most_common(5)

# [('Steven Spielberg', 26),
#  ('Woody Allen', 22),
#  ('Martin Scorsese', 20),
#  ('Clint Eastwood', 20),
#  ('Ridley Scott', 17)]