import json

filename = 'testdict.json'

def read_file():
    with open (filename, 'r') as f:
        return json.load(f)
        

show_file = read_file()
print(show_file)