#Refactoring
#if-elif-else constructs
def get_workout(day):
    if day == 'Monday':
        return 'Chest+biceps'
    elif day == 'Tuesday':
        return 'Back+triceps'
    elif day == 'Wednesday':
        return 'Core'
    elif day == 'Thursday':
        return 'Legs'
    elif day == 'Friday':
        return 'Shoulders'
    elif day in ('Saturday', 'Sunday'):
        return 'Rest'
    raise ValueError('Not a day')

workouts = {
    'Monday': 'Chest+biceps',
    'Tuesday': 'Back+triceps',
    'Wednesday': 'Core',
    'Thursday': 'Legs',
    'Friday': 'Shoulders',
    'Saturday': 'Rest',
    'Sunday': 'Rest',
}
workouts

days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()
routines = 'Chest+biceps Back+triceps Core Legs Shoulders Rest Rest'.split()

workouts2 = dict(zip(days, routines))
workouts2

def get_workout(day):
    routine = workouts.get(day)
    if routine is None:
        raise ValueError('Not a day')
    return routine
get_workout('Monday')

#counting inside a loop
days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()
i = 0
for day in days:
    i += 1
    print(f'{i}. {day}')

for i, day in enumerate(days):
    print(f'{i + 1}. {day}')

for i, day in enumerate(days, 1):
    print(f'{i}. {day}')
# 1. Monday
# 2. Tuesday
# 3. Wednesday
# 4. Thursday
# 5. Friday
# 6. Saturday
# 7. Sunday

#using builtins
numbers = range(1, 11)
list(numbers)
total = 0
for num in numbers:
    total += num
total
sum(numbers)

routines = 'Chest+biceps Back+triceps Core Legs Shoulders'.split()
timings = '45 45 30 55 45'.split()

workout_times = dict(zip(routines, timings))
workout_times

max_routine = None
max_timing = 0
for routine, timing in workout_times.items():
    timing = int(timing)
    if timing > max_timing:
        max_routine = routine
        max_timing = timing

max_routine, max_timing

#list comprehensions and generators
days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()
def get_t_days(days=days):
    t_days = []
    for day in days:
        if day[0].lower() == 't':
            t_days.append(day)
    return t_days

get_t_days()

def get_t_days(days=days):
    t_days = []
    for day in days:
        if day[0].lower() == 't':
            t_days.append(day)
    return t_days

get_t_days()