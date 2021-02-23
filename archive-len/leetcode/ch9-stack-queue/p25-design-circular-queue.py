class MyCircularQueue:

    def __init__(self, k: int) -> None:
        self.q = [None] * k
        self.maxlen = k
        self.p1_front = 0
        self.p2_rare = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.p2_rare] is None:
            self.q[self.p2_rare] = value
            self.p2_rare = (self.p2_rare + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.p1_front] is None:
            return False
        else:
            self.q[self.p1_front] = None
            self.p1_front = (self.p1_front + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.p1_front] is None else self.q[self.p1_front]

    def Rear(self) -> int:
        return -1 if self.q[self.p2_rare - 1] is None else self.q[self.p2_rare - 1]

    def isEmpty(self) -> bool:
        return self.p1_front == self.p2_rare and self.q[self.p1_front] is None

    def isFull(self) -> bool:
        return self.p1_front == self.p2_rare and self.q[self.p1_front] is not None