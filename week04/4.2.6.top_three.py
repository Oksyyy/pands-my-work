import random # import module that helps to generate random numbres

numbers = [] # create a list to store numbers that the program is going to generate

for n in range(0,10): # use for loop to ganarete 10 numbers. Function range(1,10) defines how many umebrs to be ther in the range
    n = random.randint(0,100) # generate random number 
    numbers.append(n) # add generated number to the list

print(f'10 random nmbers are {numbers}')

numbers.sort(reverse = True) # sort numebrs in descending order

print(f'The 3 top numbers are {numbers[:3]}') # print 3 top numebrs using slicing string function