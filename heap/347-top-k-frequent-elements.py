from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in Counter(nums).most_common(k)]


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
# DEBUG RUNNER END
