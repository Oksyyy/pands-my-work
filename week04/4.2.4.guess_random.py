# Program that generates a random number and trying to guess it
import random

to_guess = 30 

number = random.randrange(0,100)

while number != to_guess:
    if number < to_guess:
        print('Too low')
    else:
        print('Too high')
    number = random.randrange(0,100)
#    if number == to_guess:
#        break
print(f'Well done! Yes, the number was {to_guess}')