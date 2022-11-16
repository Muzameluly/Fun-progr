'''
"Non functional"
from random import random

def move_cars():
    for i, _ in enumerate(car_positions):
        if random() > 0.3:
            car_positions[i] += 1

def draw_car(car_position):
    print('-' * car_position)

def run_step_of_race():
    global time
    time -= 1
    move_cars()

def draw():
    print ('')
    for car_position in car_positions:
        draw_car(car_position)

time = 5
car_positions = [1, 1, 1]

while time:
    run_step_of_race()
    draw()
'''

'''
"Functional"
from random import random

def move_cars(car_positions):
    return map(lambda x: x + 1 if random() > 0.3 else x,
               car_positions)

def output_car(car_position):
    return '-' * car_position

def run_step_of_race(state):
    return {'time': state['time'] - 1,
            'car_positions': move_cars(state['car_positions'])}

def draw(state):
    print ('')
    print( '\n'.join(map(output_car, state['car_positions'])))

def race(state):
    draw(state)
    if state['time']:
        race(run_step_of_race(state))

race({'time': 5,
      'car_positions': [1, 1, 1]})
'''

'''
def outer_function(x):
    
    def inner_increment(x):
        return x + 2
    y = inner_increment(x)
    print(x, y)


outer_function(5)
'''

'''
my_list_a = [1, 2, 3]
my_list_b = [11, 22, 33]


def list_gen(my_list_a, my_list_b):
 combined_list = [my_list_a, my_list_b] 
 new_list = [i for sublist in combined_list for i in sublist]
 return new_list


print(list_gen(my_list_a, my_list_b))
'''