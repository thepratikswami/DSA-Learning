import heapq
from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)
        min_heap = list(counts.keys())
        heapq.heapify(min_heap)

        while min_heap:
            start = min_heap[0]
            for card in range(start, start + groupSize):
                if counts[card] == 0:
                    return False
                counts[card] -= 1
                if counts[card] == 0:
                    if card != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
# DEBUG RUNNER END
