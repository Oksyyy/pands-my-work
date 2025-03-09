# program that prints out a random fruit

import random # to allow for random index selection

fruits = ('avo', 'persimon', 'pear', 'pomegrant','kiwi') # list of fruits

index = random.randint(0,len(fruits)-1) # set a random index being chosen from a range

fruit = fruits(index) # setting a fruit variable to select a fruit from the list fruits using index

print(f'A random fruit is {fruit}')