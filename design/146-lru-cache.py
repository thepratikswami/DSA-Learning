class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
            return

        if len(self.map) >= self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]

        node = Node(key, value)
        self.map[key] = node
        self._add_to_front(node)


# DEBUG RUNNER START
if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))   # 1
    cache.put(3, 3)       # evicts key 2
    print(cache.get(2))   # -1
    cache.put(4, 4)       # evicts key 1
    print(cache.get(1))   # -1
    print(cache.get(3))   # 3
    print(cache.get(4))   # 4
# DEBUG RUNNER END
