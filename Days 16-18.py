from collections import Counter
import calendar
import itertools
import random
import re
import string

import requests

# List Comprehension
names = 'pybites mike bob julian tim sara guido'.split()

for name in names:
    print(name.title())

new_names = []
for name in names:
    if name[0] in first_half_alphabet:
        new_names.append(name.title())

new_names2 = [name.title() for name in names if name[0] in first_half_alphabet]
assert new_names == new_names2

# Generators
def num_gen():
    for i in range(5):
        yield i

gen = num_gen()

for i in gen:
    print(i)

options = 'red yellow blue white black green purple'.split()
def create_select_options(options=options):
    select_list = []

    for option in options:
        select_list.append(f'<option value={option}>{option.title()}</option>')

    return select_list

# list
def leap_years_lst(n=1000000):
    leap_years = []
    for year in range(1, n+1):
        if calendar.isleap(year):
            leap_years.append(year)
    return leap_years

# generator
def leap_years_gen(n=1000000):
    for year in range(1, n+1):
        if calendar.isleap(year):
            yield year