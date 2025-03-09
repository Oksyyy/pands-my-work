# Program that prompts the user to guess a number and gives hints

to_guess = 30

number = int(input('Please guess number: '))

while number != to_guess:
    if number < to_guess:
        print('Too low')
    else:
        print('Too high')
    number = int(input('Please guess again: '))
#    if number == to_guess:
#        break
print(f'Well done! Yes, the number was {to_guess}')