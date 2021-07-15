# test.py

# Implementing a stack data structure

class Stack():
    def __init__(self):
        self.stack = list()    # creates the underlying list for the stack

    def push(self, *args):
        [self.stack.append(arg) for arg in args]   #appending the pushed item to the top of the stack

    def pop(self):
        if len(self.stack) > 0:    # non-empty
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:    # non-empty
            return self.stack[-1]
        else:
            return None

    def clear(self, item = None):
        if item != None:
            if item in self.stack:
                self.stack.pop(self.stack.index(item))
                return
            else:
                return print("item not in stack")
        else:
            self.stack = []

    def __str__(self):
        return str(self.stack)

# testing
New_stack = Stack()
New_stack.push(1,[3,4],5)
print(New_stack)
New_stack.clear(1)
print(New_stack)
