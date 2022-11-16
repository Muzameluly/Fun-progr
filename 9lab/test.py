people = [{'имя': 'Маша', 'рост': 160},
    {' рост ': 'Саша', ' рост ': 80},
    {'name': 'Паша'}]

heights = map(lambda x: x['рост'],
              filter(lambda x: 'рост' in x, people))

if len(list(heights)) > 0:
    from functools import reduce
    from operator import add
    average_height = reduce(add, heights) / len(heights)