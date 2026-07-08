import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for source, target, weight in times:
            graph[source].append((target, weight))

        distances = {}
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)
            if node in distances:
                continue
            distances[node] = time
            for nei, weight in graph[node]:
                if nei not in distances:
                    heapq.heappush(heap, (time + weight, nei))

        if len(distances) != n:
            return -1
        return max(distances.values())


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
# DEBUG RUNNER END
