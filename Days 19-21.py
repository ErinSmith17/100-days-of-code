#PyBite 64 Fix a truncating zip function
import itertools

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]

def get_attendees():
    for participant in zip_longest(names, locations, confirmed, fillvalue='-'):
        print(participant)

if __name__ == '__main__':
    get_attendees()

# Traffic Light practice
from time import sleep
import itertools
import random

colours = 'Red Green Amber'.split()
rotation = itertools.cycle(colours)

def rg_timer():
    return random.randint(3, 7)

def light_rotation(rotation):
    for colour in rotation:
        if colour == 'Amber':
            print('Caution! The light is %s' % colour)
            sleep(3)
        elif colour == 'Red':
            print('STOP! The light is %s' % colour)
            sleep(rg_timer())
        else:
            print('Go! The light is %s' % colour)
            sleep(rg_timer())

if __name__ == '__main__':
    light_rotation(rotation)
    