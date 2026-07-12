class MyCircularQueue:
    def __init__(self, k: int):
        self.data = [0] * k
        self.capacity = k
        self.head = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        tail = (self.head + self.count) % self.capacity
        self.data[tail] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        tail = (self.head + self.count - 1) % self.capacity
        return self.data[tail]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


# DEBUG RUNNER START
if __name__ == "__main__":
    queue = MyCircularQueue(3)
    print(queue.enQueue(1))  # True
    print(queue.enQueue(2))  # True
    print(queue.enQueue(3))  # True
    print(queue.enQueue(4))  # False (full)
    print(queue.Rear())      # 3
    print(queue.isFull())    # True
    print(queue.deQueue())   # True
    print(queue.enQueue(4))  # True
    print(queue.Rear())      # 4
    print(queue.Front())     # 2
# DEBUG RUNNER END
