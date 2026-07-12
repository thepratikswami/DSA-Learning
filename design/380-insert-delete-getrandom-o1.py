import random


class RandomizedSet:
    def __init__(self):
        self.map = {}       # value -> index in self.values
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        idx = self.map[val]
        last = self.values[-1]
        # Move the last value into the slot of the one being removed.
        self.values[idx] = last
        self.map[last] = idx
        self.values.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# DEBUG RUNNER START
if __name__ == "__main__":
    rset = RandomizedSet()
    print(rset.insert(1))    # True
    print(rset.remove(2))    # False
    print(rset.insert(2))    # True
    print(rset.getRandom())  # 1 or 2
    print(rset.remove(1))    # True
    print(rset.insert(2))    # False (already present)
    print(rset.getRandom())  # 2
# DEBUG RUNNER END
