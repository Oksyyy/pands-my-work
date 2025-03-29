filename = 'count.txt'

def read_num():
    with open(filename) as f:
        number = int(f.read())
    return number
 
count = read_num()
print(count)