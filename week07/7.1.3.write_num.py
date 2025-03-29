filename = 'count.txt'

def write_num(number):
    with open(filename, 'w+') as f:
       new_number= f.write(str(number))

number = 0
num = write_num(number)
