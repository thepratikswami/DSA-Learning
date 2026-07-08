from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord("a")] += 1
            groups[tuple(counts)].append(word)

        return list(groups.values())


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# DEBUG RUNNER END
