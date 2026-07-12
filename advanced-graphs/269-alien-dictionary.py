from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        indegree = {ch: 0 for word in words for ch in word}

        for first, second in zip(words, words[1:]):
            min_len = min(len(first), len(second))
            # Invalid: a longer word appears before its own prefix.
            if len(first) > len(second) and first[:min_len] == second[:min_len]:
                return ""
            for a, b in zip(first, second):
                if a != b:
                    if b not in adj[a]:
                        adj[a].add(b)
                        indegree[b] += 1
                    break

        queue = deque(ch for ch in indegree if indegree[ch] == 0)
        order = []

        while queue:
            ch = queue.popleft()
            order.append(ch)
            for nei in adj[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        if len(order) < len(indegree):
            return ""  # cycle detected
        return "".join(order)


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
# DEBUG RUNNER END
