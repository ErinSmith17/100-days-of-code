#Measuring preformance
import research
import os
import csv
import collections
from typing import List

data = []

Record = collections.namedtuple(
    'Record',
    'date,actual_min_temp,actual_max_temp,actual_precipitation'
)


def init():
    if data:
        return

    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'seattle.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            record = parse_row(row)
            data.append(record)


def parse_row(row):
    row['actual_min_temp'] = int(row['actual_min_temp'])
    row['actual_max_temp'] = int(row['actual_max_temp'])
    row['actual_precipitation'] = float(row['actual_precipitation'])

    record = Record(
        date=row.get('date'),
        actual_min_temp=row.get('actual_min_temp'),
        actual_max_temp=row.get('actual_max_temp'),
        actual_precipitation=row.get('actual_precipitation'),
    )

    return record

# Before simpler parse_row:
# 99    0.050    0.001    0.759    0.008 research.py:17(init)
# 36135    0.321    0.000    0.351    0.000 research.py:30(parse_row)
#
# After simplification:
# 99    0.052    0.001    0.554    0.006 research.py:14(init)
# 36135    0.111    0.000    0.159    0.000 research.py:27(parse_row)


def hot_days() -> List[Record]:
    return sorted(data, key=lambda r: -r.actual_max_temp)


def cold_days() -> List[Record]:
    return sorted(data, key=lambda r: r.actual_min_temp)


def wet_days() -> List[Record]:
    return sorted(data, key=lambda r: -r.actual_precipitation)

def main():
    print("Weather research for Seattle, 2014-2015")
    print()

    research.init()

    hot_days = research.hot_days()
    cold_days = research.cold_days()
    wet_days = research.wet_days()

    print("The hottest 5 days:")
    for idx, d in enumerate(hot_days[:5]):
        print("{}. {} F on {}".format(idx + 1, d.actual_max_temp, d.date))
    print()
    print("The coldest 5 days:")

    for idx, d in enumerate(cold_days[:5]):
        print("{}. {} F on {}".format(idx + 1, d.actual_min_temp, d.date))
    print()
    print("The wettest 5 days:")

    for idx, d in enumerate(wet_days[:5]):
        print("{}. {} inches of rain on {}".format(idx + 1, d.actual_precipitation, d.date))


if __name__ == '__main__':
    for _ in range(1, 100):
        main()