import random

min_range = int(input('Enter minimum number of a range you want your random number be in: '))
max_range = int(input('Enter maximum number of a range you want your random number be in: '))

number = random.randint(min_range,max_range)

print(f'Here is a random number {number}')