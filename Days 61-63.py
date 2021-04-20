#Using the Github API with Python
from collections import namedtuple
import os

from github import Github, InputFileContent
gh = Github()
gh
gh.rate_limiting
pb = gh.get_user('pybites')
pb

#getting help in python

dir(pb)
help(pb.get_repos)
pb.get_repos()
Repo = namedtuple('Repo', 'name stars forks')
def get_repo_stats(user, n=5):
    """We did this exercise in our own 100 Days of Code:
       https://github.com/pybites/100DaysOfCode/blob/master/084/ghstats.py"""
    repos = []
    for repo in user.get_repos():
        if repo.fork:
            continue

        repos.append(Repo(name=repo.name,
                          stars=repo.stargazers_count,
                          forks=repo.forks_count))

    return sorted(repos, key=lambda x: x.stars, reverse=True)[:n]
get_repo_stats(pb)
mk = gh.get_user('mikeckennedy')
get_repo_stats(mk)
token = os.environ['GH_GIST_CREATE_TOKEN']
gh = Github(token)
gh
gh.rate_limiting
code = '''
from collections import namedtuple

Repo = namedtuple('Repo', 'name stars forks')


def get_repo_stats(user, n=5):
    """Takes a Github user object and returns the top n most popular repos by star count,
       skips forks."""
    repos = []
    for repo in user.get_repos():
        if repo.fork:
            continue

        repos.append(Repo(name=repo.name,
                          stars=repo.stargazers_count,
                          forks=repo.forks_count))

    return sorted(repos, key=lambda x: x.stars, reverse=True)[:n]
'''

me.create_gist(True,
               {"repo_stats.py": InputFileContent(code)},
               "Get GH user's most popular repos")
for gist in gh.get_user('pybites').get_gists():
    print(f'{gist.description} ({gist.created_at})')
    print(f'https://gist.github.com/{gist.id}')
    import pdb; pdb.set_trace()