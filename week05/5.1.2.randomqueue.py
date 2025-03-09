import random

queue = []
range_to = 100

while len(queue) < 10:
    a = random.randint(0,range_to)
    queue.append(a)
print(f'Queue is {queue}')

while len(queue)>0:
    print (f'The current number is {queue.pop(0)} and the queue is {queue}')

print('The queue is now empty')
