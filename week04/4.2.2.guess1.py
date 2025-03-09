# Program that prompts the user to guess a number

to_guess = 30

number = int(input('Please guess number: '))

while number != to_guess:
    print('Wrong')
    number = int(input('Please guess again: '))
#    if number == to_guess:
#        break
print(f'Well done! Yes, the number was {to_guess}')