# try out the Python queue functions
from collections import deque

# TODO: create a new empty deque object that will function as a queue
queue = deque()

# TODO: add some items to the queue


queue.append(1)
queue.append(11)
queue.append(12)
queue.append(13)

# TODO: print the queue contents

print(queue)

# TODO: pop an item off the front of the queue

queue.popleft()

print(queue)
