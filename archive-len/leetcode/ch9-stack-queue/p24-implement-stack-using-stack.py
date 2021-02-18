
class Stack:
    def __init__(self) -> None:
        self.input = []
        self.output = []

    def push(self, data):
        self.input.append(data)

    def pop(self):
        self.peek()

    def empty(self):
        return self.input == [] and self.output == []

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
