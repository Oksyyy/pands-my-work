import statistics # to use average fuction  statistics.mean()

numbers = [] # create a list of numbers

n = int(input('Enter a number: ')) # prompt a user to enter the first number

while n != 0: # use while loop to add numbers into the list using .append() function
    numbers.append(n)
    n = int(input('Enter a number (0 to quit): ')) # keep prompting user to enter numbers until they enter 0

for n in numbers: # use for loop to print numbers from the list 1 by 1
    print(n)
  
average = statistics.mean(numbers)
print(f'The average is {average}')
