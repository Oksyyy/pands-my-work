import json

some_dict = {
    'name':'Oksana',
    'activity':'yoga'
}
filename = 'testdict.json'
def store_data():
    with open(filename, 'w+') as f:
        json.dump(some_dict, f)

read = store_data()

with open(filename) as f:
    for line in f:
        print(line)