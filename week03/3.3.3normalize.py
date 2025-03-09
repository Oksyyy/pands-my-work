string = str(input('Please enter a string: '))

raw_len = len(string) # count number of characters in input string

normalised_str =  string.lower().strip() # use fuction lower() to convert to lower case
# and use function strip() to remove leading / trailing spaces

print(f'The string normilized is: {normalised_str}')

raw_len = len(string) # count number of characters in input string
normalized_len = len(normalised_str) # count number of characters in innormalized string

print(f'We reduced the input string from {raw_len} to {normalized_len} characters')
