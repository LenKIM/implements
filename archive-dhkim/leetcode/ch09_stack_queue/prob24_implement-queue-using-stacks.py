"""
https://leetcode.com/problems/implement-queue-using-stacks/
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.output_stack) == 0:
            for _ in range(len(self.input_stack)):
                tmp = self.input_stack.pop()
                self.output_stack.append(tmp)

        return self.output_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.output_stack) == 0:
            for _ in range(len(self.input_stack)):
                tmp = self.input_stack.pop()
                self.output_stack.append(tmp)

        return self.output_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.input_stack) == 0 and len(self.output_stack) == 0


if __name__ == "__main__":
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()

    data = [1,2,3,4,5,6,7]
    for n in data:
        obj.push(n)
    print(f"myqueue peek : {obj.peek()}")
    for _ in range(len(data)):
        print(obj.pop())
    print(f"myqueue is empty? : {obj.empty()}")

    data = [8,9,10,11,12]
    for n in data:
        obj.push(n)
    print(f"myqueue peek : {obj.peek()}")
    for _ in range(len(data)):
        print(obj.pop())
    print(f"myqueue is empty? : {obj.empty()}")
