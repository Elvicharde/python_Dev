#queue.py

# This implements a queue structure
# A queue has two methods: enqueue and de-queue

class Queue():
    def __init__(self):
        self.queue = list()    # default list for performing queue

    def enqueue(self, *args):
        [self.queue.append(arg) for arg in args]

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def get_size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)

my_queue = Queue()
my_queue.enqueue(1,2,3)
print(my_queue)
print(f"{my_queue.dequeue()} dequeued")
print(my_queue)
print(f"{my_queue.dequeue()} dequeued")
print(my_queue)
print(f"{my_queue.dequeue()} dequeued")
print(my_queue)
print(f"{my_queue.dequeue()} dequeued")




