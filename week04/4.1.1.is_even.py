# is_even.py
# Program that prompts user to input a number and print out if that number is even or odd
# Author: Oksana Abrosimova

number = int(input('Enter a number: '))

if number % 2 == 0:
    print(f'{number} is an even number')
else:
    print(f'{number} is an odd number')

