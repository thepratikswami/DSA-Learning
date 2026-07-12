import heapq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-count for count in counts.values()]
        heapq.heapify(heap)

        time = 0
        cooldown = deque()  # entries of (ready_time, remaining_count)

        while heap or cooldown:
            time += 1
            if heap:
                remaining = heapq.heappop(heap) + 1
                if remaining != 0:
                    cooldown.append((time + n, remaining))
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(heap, cooldown.popleft()[1])

        return time


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))
# DEBUG RUNNER END
