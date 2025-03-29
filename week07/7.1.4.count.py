# Existing file contains a number (started from 0)
filename = 'count.txt'

# Create a function to read the number from the file count.txt
def read_num():
    # Use with open() function to open file for reading
    with open(filename) as f:
        # Use read() funtion to read the file. Also use int function as files contains string characters only
        number = int(f.read())    
    # Return the number from count.txt file
    return number

# Create function that will write / update the number in the file
def write_num(number):  
    # Open file count.txt for writing 
    with open(filename, 'wt') as f:    
    # Use write() function to write into the file
        new_number= f.write(str(number))


# Call function read_num()to get the current number from the file
number = read_num()

# Update that number to the number + 1
number = number + 1 

print(f'We have run this program {number} times')

# Call write_num function to write the new number into the file 
# This will update the existing number to the new one
count = write_num(number)
