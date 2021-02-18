import collections


class Stack:
    def __init__(self) -> None:
        self.q = collections.deque()

    def push(self, data):
        self.q.append(data)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0