import collections


class MyQueue(object):
    def __init__(self):
        self.input = []
        self.output = []

    def peek(self):
        if not self.output:
            while len(self.input) != 0:
                self.output.append(self.input.pop())
        return self.output[-1]

    def pop(self):
        self.peek()
        return self.output.pop()

    def put(self, value):
        self.input.append(value)

    def is_empty(self):
        return len(self.input) == 0



queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())