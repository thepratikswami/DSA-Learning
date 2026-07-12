from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)  # reverse sort so pop() gives smallest lex.

        route = []
        stack = ["JFK"]

        while stack:
            airport = stack[-1]
            if graph[airport]:
                stack.append(graph[airport].pop())
            else:
                route.append(stack.pop())

        return route[::-1]


# DEBUG RUNNER START
if __name__ == "__main__":
    print(
        Solution().findItinerary(
            [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        )
    )
# DEBUG RUNNER END
