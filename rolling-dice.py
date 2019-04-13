import random
import numpy
from collections import Counter

def rolling_dice():
    return random.randrange(1,7)

def extract_data():
    array = []
    for x in range(100):
        rolled_number = rolling_dice()
        array.append(rolled_number)

    temp = Counter(array)
    return('...temp: ', temp)


extract_data()
