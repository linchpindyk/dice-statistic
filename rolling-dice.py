from __future__ import division
import random
import numpy
from collections import Counter

def roll_dice():
    return random.randrange(1,7)

def get_probability(num_repeat):
    array = []
    for x in range(int(num_repeat)):
        rolled_number = roll_dice()
        array.append(rolled_number)

    statistic = Counter(array)

    print('``````````````rolling die``````````````')
    print('`')

    for y in range(1,7):
        probability = (int(statistic[y]) / int(num_repeat)) * 100
        print('`   Probability of getting %s: %s%%' % (y, round(probability, 1)))

    print('`')
    print('```````````````end result``````````````')

def execute_program():
    times_rolled = input('How many times do you want to roll? ')
    get_probability(times_rolled)

execute_program()
