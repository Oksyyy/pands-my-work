import os

filename = 'count1.txt'
if not os.path.isfile(filename):
    print('File does not exists')

    def write_num(number): 
        with open(filename, 'w') as f: 
            f.write(str(number))
    number = 0
    file = write_num(number)
    print(file)
