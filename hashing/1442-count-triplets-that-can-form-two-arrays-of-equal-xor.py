from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = {0: 1}
        total_indices = {0: 0}
        prefix = 0
        ans = 0

        for i, num in enumerate(arr, start=1):
            prefix ^= num
            if prefix in count:
                ans += count[prefix] * (i - 1) - total_indices[prefix]
            count[prefix] = count.get(prefix, 0) + 1
            total_indices[prefix] = total_indices.get(prefix, 0) + i

        return ans


# DEBUG RUNNER START
if __name__ == "__main__":
    print(Solution().countTriplets([2, 3, 1, 6, 7]))
# DEBUG RUNNER END
